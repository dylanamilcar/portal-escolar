from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = "database/escuela.db"


def conectar_db():
    conexion = sqlite3.connect(DATABASE)
    conexion.row_factory = sqlite3.Row
    return conexion


def crear_tabla_buzon():
    conexion = conectar_db()
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS buzon (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            mensaje TEXT NOT NULL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conexion.commit()
    conexion.close()


@app.route("/")
def inicio():
    ultimo_mensaje = 0
    try:
        conexion = conectar_db()
        fila = conexion.execute("SELECT MAX(id) AS ultimo FROM buzon").fetchone()
        ultimo_mensaje = fila["ultimo"] or 0
        conexion.close()
    except sqlite3.Error:
        pass
    return render_template("index.html", ultimo_mensaje=ultimo_mensaje)


@app.route("/escuela")
def escuela():
    return render_template("escuela.html")


@app.route("/oferta")
def oferta():
    return render_template("oferta.html")


@app.route("/programas")
def programas():
    return render_template("programas.html")


@app.route("/instalaciones")
def instalaciones():
    return render_template("instalaciones.html")


@app.route("/actividades")
def actividades():
    return render_template("actividades.html")


@app.route("/noticias")
def noticias():
    return render_template("noticias.html")


@app.route("/buzon", methods=["GET", "POST"])
def buzon():
    conexion = conectar_db()

    if request.method == "POST":
        tipo = request.form.get("tipo", "").strip()
        mensaje = request.form.get("mensaje", "").strip()

        if tipo and mensaje and len(mensaje) <= 500:
            conexion.execute(
                "INSERT INTO buzon (tipo, mensaje) VALUES (?, ?)",
                (tipo, mensaje)
            )
            conexion.commit()

        conexion.close()
        return redirect(url_for("buzon"))

    publicaciones = conexion.execute("""
        SELECT id, tipo, mensaje, fecha
        FROM buzon
        ORDER BY id ASC
    """).fetchall()
    conexion.close()

    return render_template("buzon.html", publicaciones=publicaciones)


if __name__ == "__main__":
    crear_tabla_buzon()
    app.run(debug=True)

from flask import Flask, render_template, request, redirect
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
    return render_template("index.html")


@app.route("/buzon", methods=["GET", "POST"])
def buzon():

    conexion = conectar_db()

    if request.method == "POST":

        tipo = request.form.get("tipo")
        mensaje = request.form.get("mensaje")

        if tipo and mensaje:

            conexion.execute(
                """
                INSERT INTO buzon (tipo, mensaje)
                VALUES (?, ?)
                """,
                (tipo, mensaje)
            )

            conexion.commit()

        conexion.close()

        return redirect("/buzon")

    publicaciones = conexion.execute(
        """
        SELECT id, tipo, mensaje, fecha
        FROM buzon
        ORDER BY fecha DESC
        """
    ).fetchall()

    conexion.close()

    return render_template(
        "buzon.html",
        publicaciones=publicaciones
    )


if __name__ == "__main__":
    crear_tabla_buzon()
    app.run(debug=True)
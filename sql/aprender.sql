CREATE DATABASE MiBaseDeDatos;
GO

USE MiBaseDeDatos;
GO

CREATE TABLE Clientes (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Nombre NVARCHAR(100) NOT NULL,
    Correo NVARCHAR(100),
    FechaRegistro DATE DEFAULT GETDATE()
);
GO

INSERT INTO Clientes (Nombre, Correo)
VALUES (N'Ana López', 'ana@correo.com');

SELECT * FROM Clientes;
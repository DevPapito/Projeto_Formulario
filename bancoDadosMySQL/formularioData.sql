CREATE DATABASE formularioData;
USE formularioData;

CREATE TABLE clientes(
	ID_clientes INT KEY AUTO_INCREMENT NOT NULL,
    NameUser VARCHAR(150),
    EmailUser VARCHAR(100),
    DescriptionUser VARCHAR(500)

);

-- visão genérica
SELECT * 
FROM clientes;

-- ordem descrescente
SELECT *
FROM CLIENTES
ORDER BY ID_clientes desc;

-- pesquisa por dominios de Email: GMAIL
SELECT NameUser as "Usuário",EmailUser as "Dominio Gmail"
FROM CLIENTES
WHERE EmailUser LIKE ('@g%');

-- pesquisa por dominios de Email: Yahoo.com
SELECT NameUser as "Usuário",EmailUser as "Dominio Yahoo"
FROM CLIENTES
WHERE EmailUser LIKE ('@y%');

-- agrupar por emails
SELECT * 
FROM CLIENTES
GROUP BY EmailUser;

-- Achar "PROGRAMADOR" em DescriptionUser
SELECT NameUser,DescriptionUser 
FROM CLIENTES
WHERE DescriptionUser LIKE ("programador");
SELECT * FROM clientes;
delete FROM clientes
WHERE ID_clientes = 3;

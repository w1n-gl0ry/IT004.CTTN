-- delete database if exist 

DROP DATABASE IF EXISTS TRUONGHOC1;

-- create db TRUONGHOC1

CREATE DATABASE TRUONGHOC1;

-- use db TRUONGHOC1;

USE TRUONGHOC1;

-- delete table HOC if exist 

DROP TABLE IF EXISTS HOC;

-- delete table HS if exist

DROP TABLE IF EXISTS HS;

-- delete table HOC if exist 

DROP TABLE IF EXISTS HOC;

-- create table TRUONG

CREATE TABLE TRUONG (
    MATR VARCHAR(100) PRIMARY KEY not null,      -- PRIMARY KEY (MATR)
    TENTR VARCHAR(100) not null,       -- TRUONG name
    DCHITR VARCHAR(255) not null     -- TRUONG address
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci; -- encoding UTF-8 (utf8mb4) to help VIETNAMESE font 


-- create table HS

CREATE TABLE HS (
    MAHS VARCHAR(100) PRIMARY KEY not null,         -- PRIMARY KEY (MAHS)
    HO VARCHAR(100) not null,          -- surname
    TEN VARCHAR(100) not null,        -- name
    CCCD VARCHAR(100) UNIQUE,   -- ID card
    NTNS DATE not null,        -- birthday
    DCHI_HS VARCHAR(255) not null    -- HS address
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci; -- encoding UTF-8 (utf8mb4) to help VIETNAMESE font

-- create table HOC

CREATE TABLE HOC (
    MATR VARCHAR(100) not null,    -- MATR 
    MAHS VARCHAR(100) not null,  -- MAHS
    NAMHOC VARCHAR(100),      -- NAMHOC
    DIEMTB FLOAT not null, -- average score
    XEPLOAI VARCHAR(100) not null,  -- rank
    KQUA VARCHAR(100) not null,  -- result

    PRIMARY KEY(MATR, MAHS, NAMHOC),     -- PRIMARY KEY
    CONSTRAINT HOC_TRUONG_FK FOREIGN KEY(MATR) REFERENCES TRUONG(MATR),   -- FOREIGN KEY that references to TRUONG table  
    CONSTRAINT HOC_HS_FK FOREIGN KEY(MAHS) REFERENCES HS(MAHS)       -- FOREIGN KEY that references to HS table  
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci; -- encoding UTF-8 (utf8mb4) to help VIETNAMESE font

ALTER TABLE HOC DROP FOREIGN KEY HOC_TRUONG_FK;
ALTER TABLE HOC DROP FOREIGN KEY HOC_HS_FK;

ALTER TABLE HOC ADD CONSTRAINT HOC_TRUONG_FK FOREIGN KEY (MATR) REFERENCES TRUONG (MATR);
ALTER TABLE HOC ADD CONSTRAINT HOC_HS_FK FOREIGN KEY (MAHS) REFERENCES HS (MAHS);
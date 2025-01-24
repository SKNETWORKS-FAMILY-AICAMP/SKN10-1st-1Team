Use mysql;                        -- 계정생성 및 권한부여
Create user 'dreamteam'@'%'
    identified by '1234';
create user 'faq_user'@'%'
    identified by 'faq1234';
Select * from user;

drop database if exists 자동차현황DB;
CREATE DATABASE 자동차현황DB;
CREATE DATABASE faq_db;
grant all privileges
    on 자동차현황DB.*
    to 'dreamteam'@'%';

grant all privileges
    on faq_db.*
    to 'faq_user'@'%';
USE 자동차현황DB;

CREATE TABLE 차종등록현황 (
    차종ID INT AUTO_INCREMENT PRIMARY KEY, -- 고유 식별자
    차종명 VARCHAR(50) NOT NULL,
    등록연도 INT NOT NULL,              -- VARCHAR보다 INT로 설정해야지 연산 더 빠름
    등록대수 INT NOT NULL
);

CREATE TABLE 지역등록현황 (
    지역ID INT AUTO_INCREMENT PRIMARY KEY, -- 지역 고유 ID
    지역명 VARCHAR(50) NOT NULL,    -- 지역명 (서울, 부산 등)
    등록연도 INT NOT NULL,
    등록대수 INT NOT NULL
);


CREATE TABLE 종합관리 (
    종합ID INT AUTO_INCREMENT PRIMARY KEY,  -- 고유 식별자
    차종ID INT NOT NULL,                    -- 차종 등록 테이블 참조
    지역ID INT NOT NULL,                    -- 지역 등록 테이블 참조
    등록연도 INT NOT NULL,                  -- 연도
    등록대수 INT NOT NULL,                  -- 등록대수
    FOREIGN KEY (차종ID) REFERENCES 차종등록현황(차종ID) ON DELETE CASCADE,
    FOREIGN KEY (지역ID) REFERENCES 지역등록현황(지역ID) ON DELETE CASCADE,
    UNIQUE KEY (차종ID, 지역ID, 등록연도)   -- 복합 고유 키
);

USE faq_db;
CREATE TABLE faq_category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,  -- Auto-increment primary key
    category VARCHAR(20) NOT NULL,     -- Category column
    question TEXT NOT NULL,            -- Question column
    answer TEXT NOT NULL               -- Answer column
);

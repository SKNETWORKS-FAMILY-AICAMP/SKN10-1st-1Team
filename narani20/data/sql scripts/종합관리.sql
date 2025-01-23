/*모든 INSERT 실행 후 실행 하기 */

INSERT INTO 종합관리 (차종ID, 지역ID, 등록연도, 등록대수)
SELECT
    차종등록현황.차종ID,
    지역등록현황.지역ID,
    지역등록현황.등록연도,
    SUM(지역등록현황.등록대수) AS 등록대수
FROM
    차종등록현황
JOIN
    지역등록현황
ON
    차종등록현황.등록연도 = 지역등록현황.등록연도
GROUP BY
    차종등록현황.차종ID,
    지역등록현황.지역ID,
    지역등록현황.등록연도
ON DUPLICATE KEY UPDATE
    등록대수 = 등록대수 + VALUES(등록대수);
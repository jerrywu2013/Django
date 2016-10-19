```
CREATE VIRTUAL TABLE test USING fts4(subject, keyword);
INSERT INTO test(docid, subject, keyword) VALUES(1, '高雄市旗津區廟前路61號', '高雄市,旗津區,廟前路,61,號');
INSERT INTO test(docid, subject, keyword) VALUES(2, '國立臺灣科技大學', '國立,臺灣,科技,大學');
INSERT INTO test(docid, subject, keyword) VALUES(3, '華創車電中心',  '華創,車電,中心,政益');

SELECT * FROM mail WHERE subject MATCH '中心*';  
```

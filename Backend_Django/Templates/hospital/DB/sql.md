

```sql
CREATE TABLE Images (
    image_id SERIAL PRIMARY KEY,
    file_path VARCHAR(255),
    uploaded_timestamp TIMESTAMP,
    source VARCHAR(100)
);

CREATE TABLE Analysis_Results (
    result_id SERIAL PRIMARY KEY,
    image_id INTEGER REFERENCES Images(image_id),
    detected_text TEXT,
    detected_objects TEXT,
    analysis_timestamp TIMESTAMP
);

CREATE TABLE Actions_Log (
    action_id SERIAL PRIMARY KEY,
    result_id INTEGER REFERENCES Analysis_Results(result_id),
    action_description TEXT,
    action_timestamp TIMESTAMP
);
```



<!-- 예시 -->
# 이미지 테이블

```html
<img src="{% static 'image/barcode/IMG_7401.jpeg' %}" style="height: 100%;"/>
```

예를 들어, 위에 처럼 작성해야 한다면, 아래 처럼 path가 들어가서 불러올 수 있게 만들어야 한다.

```sql
INSERT INTO Images (image_id, file_path, uploaded_timestamp, source) VALUES
(00000001,'image/barcode/IMG_7401.jpeg', '2024-05-13 12:00:00', 'Camera'),
(00000002,'image/barcode/IMG_7402.jpeg', '2024-05-13 12:05:00', 'Camera');
```



# 작업 테이블 예시
```sql
INSERT INTO Analysis_Results (result_id,image_id, detected_text, detected_objects, analysis_timestamp) VALUES
(00000001, 'Store Name: ABC Mart', 'Sign, Door', '2024-05-13 14:00:00'),
(00000001, 'Exit Sign', 'Sign', '2024-05-13 14:05:00'),
(00000001, 'No Parking', 'Sign, Car', '2024-05-13 14:10:00'),
(00000001, 'Menu: Pizza, Pasta', 'Menu Board', '2024-05-13 14:15:00'),
(00000001, 'Caution: Wet Floor', 'Sign', '2024-05-13 14:20:00'),
(00000002, 'Sale up to 50% off', 'Sign, Clothes', '2024-05-13 14:25:00'),
(00000002, 'Keep off the grass', 'Sign, Grass', '2024-05-13 14:30:00'),
(00000002, 'Emergency Exit', 'Sign, Door', '2024-05-13 14:35:00'),
(00000002, 'Ingredients: Flour, Sugar', 'Label', '2024-05-13 14:40:00'),
(00000002, 'Street Name: Elm Street', 'Street Sign', '2024-05-13 14:45:00');
```
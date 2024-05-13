

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
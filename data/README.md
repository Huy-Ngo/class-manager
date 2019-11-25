This is the directory for data of the class. The data should be stored in this format:

```json
{
    "id": 0,
    "surname": "Nguyen Van",
    "name": "A",
    "student-id": "BI0-000",
    "class": "ICT"
}
```

Here the id is a number for internal use, not the one that's assigned by the school.

Here is the standard format, and it can be generated from a .xlsx, or .csv file with the following command:


```shell script
python convert --file-name=student-list.xlsx
```

(So far only .xlsx is implemented)

Note that: you should names the fields correctly with lower case and words separated with dash.
The header line should be placed at 1st row of the file. The sheet should be named "student list".
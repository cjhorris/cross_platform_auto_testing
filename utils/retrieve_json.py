SAMPLE_JSON = {
    "total_rows": 184,
    "offset": 0,
    "rows": [
        {
            "id": "SIT/DRA/2020/001",
            "key": "SIT/DRA/2020/001",
            "value": {
                "rev": "645-2f3611a220ac5cc86186764304f2e4b5"
            }
        },
        {
            "id": "SIT/DRA/2020/002",
            "key": "SIT/DRA/2020/002",
            "value": {
                "rev": "630-19697a00a20857b46406c9ed55fa75da"
            },
            "counter1": [
                {
                    "id": "1234",
                    "counter2": [
                        {
                            "id": "1234"
                        }
                    ]
                }
            ]
        }
    ],
    "date": "12/12/2001"
}

result = []


def retrieve_from_dict(json_input: dict):
    for json_key, json_value in json_input.items():

        if isinstance(json_value, dict):
            retrieve_from_dict(json_value)

        if isinstance(json_value, list):
            for item in json_value:
                retrieve_from_dict(item)

        result_dict = {json_key: json_value}
        result.append(result_dict)


retrieve_from_dict(SAMPLE_JSON)
print(result)

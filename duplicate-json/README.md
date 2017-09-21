### Duplicate JSON field

###### Script to duplicate a field from a JSON object

### Requirements:

Use any language or program you are aware of to duplicate a field from a json file
programmatically.
Ex: Your JSON file looks like this:
```
{[
{"id":"123456","field1":"data1","field2":"data2"},
{"id":"123457","field1":"data1","field2":"data2"},
…
{"id":"200301","field1":"data1","field20000":"data20000"},
]}
and should end up like this
{[
{"_id":"123456","id":"123456","field1":"data1","field2":"data2"},
{"_id":"123457","id":"123457","field1":"data1","field2":"data2"},
…
{"_id":"200301","id":"200301","field1":"data1","field20000":"data20000"},
]}
```

**NOTE**: JSON file must have the exact layout of the JSON object(s) in `example.json`

### How to run:

```
kendall@kendall-XPS-8500:~/Development/interview-project/duplicate-json$ python duplicate-json.py -f example.json
duplicated JSON file:
{'items': [{'onclick': 'CreateNewDoc()', '_onclick': 'CreateNewDoc()', 'value': 'New'}, {'onclick': 'OpenDoc()', '_onclick': 'OpenDoc()', 'value': 'Open'}, {'onclick': 'CloseDoc()', '_onclick': 'CloseDoc()', 'value': 'Close'}]}
```

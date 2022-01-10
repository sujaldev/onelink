# Documentation

## Raw Config:

This is the config data converted from JSON received through pastebin api to a dictionary. The config should follow the
following format:

```json
{
  "type": "",
  "schedule": [
    [
      {
        "start": "",
        "end": "",
        "redirect_url": "",
        "override_end_day": ""
      },
      {
        "start": "",
        "end": "",
        "redirect_url": "",
        "override_end_day": ""
      }
    ],
    [],
    []
  ]
}
```

- `type`: either `daily` or `weekdays`
- `schedule`: schedule is a list that must contain 7 empty or non-empty lists
    - `day schedule`: each list inside `schedule` is termed as a day schedule and is automatically linked to a day based
      on the index number, example: index 0 belongs to monday. It contains `events` that start on its respective day but
      don't necessarily end on the same day.
        - `event`: it is a dictionary containing 3 required items and one optional
            - `start`: __(Required)__ time stamp in format `%d %H:%M`. for `%d` Monday is 01 and Sunday is 07 and also
              must be equal to parent list's day.
            - `end`: __(Required)__ same as above, except the date in `%d` doesn't have to equal the parent list's day.
            - `redirect_url`: __(Required)__ the url that belongs to the given event's time range.
            - `override_end_day`: __(Optional)__ when the end time stamp does not belong to parent list's day, this
              parameter has to be specified.

## Parser (\_\_init__.py)

This is the main parser which will parse the raw_config and determine which sub parser to be used. It will finally
return the parsed results.

### Sub Parsers

#### Weekdays Parser

It creates a cyclic doubly linked list data structure for the weekdays.
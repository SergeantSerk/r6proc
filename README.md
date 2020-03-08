# r6proc
Rainbow Six Siege player profile snapshotting and storing program.

## Description
This app snapshots players' core stats (profile, ranked and overall) and saves them to a CSV file. Note that this needs to be manually run through an automation script (see start.sh).

## Example
Running this sample program will attempt to save players' snapshots in the `player` folder. Make sure this exists before running.

```python
from r6proc import r6proc

uuids = [
  '0a32319d-f7de-4ec1-a845-25ee53f978a7'
]

r6proc = r6proc()
r6proc.process_uuids(uuids)
```

## License
All Rights Reserved © 2020. No use without explicit permission of the owner/contributors.

Note: This license will change sooner to relax rights and public usage.

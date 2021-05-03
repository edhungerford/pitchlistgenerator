# pitchlistgenerator
A personal tool for generating one-shot pitches for my tabletop group's one-shot nights.

### Instructions
1. Ensure you have the latest version by cloning this repo.
2. Edit any cell in the first sheet of `oneshots.xlsx`. This will randomize the values in the rightmost column, which is how we get our table in the second sheet.
3. Refresh the query found in the second sheet of `oneshot.xlsx`.
4. Save `oneshots.xlsx` and close it. Do not forget this step.
5. Run either `oneshots2markdown.py` or `generate.bat`. If you run `oneshots2markdown.py`, you'll have to open `index.html` on your own.
6. Marvel at the data in `index.html`.
7. Copy a chunk of text in the Markdown column and paste it into Discord. (You will have to paste it in chunks to avoid Discord's message length limit.)
8. Replace the variables in brackets ([EMOJI], [DATE], etc.) with the proper values. Send the message.
9. Repeat steps 6 and 7 for each chunk of text.
10. Wait for the other people in the group to vote. Cry while they wait until the last minute.
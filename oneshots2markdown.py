import pandas as pd

def convertToRichText(string):
    string = string.replace(">","<blockquote>")
    string = string.replace("@\n","</blockquote>")
    string = string.replace("@","</blockquote>")
    stringArray = string.split("**")
    string=""
    for i in range(len(stringArray)):
        if i%2==0:
            string = string + stringArray[i] + "<b>"
        else:
            string = string + stringArray[i] + "</b>"
    stringArray = string.split("__")
    string=""
    for i in range(len(stringArray)):
        if i%2==0:
            string = string + stringArray[i] + "<u>"
        else:
            string = string + stringArray[i] + "</u>"
    stringArray = string.split("*")
    string=""
    for i in range(len(stringArray)):
        if i%2==0:
            string = string + stringArray[i] + "<i>"
        else:
            string = string + stringArray[i] + "</i>"
    return(string.replace("\n","<br>"))


def main():
    data = pd.read_excel (r'oneshots.xlsx', sheet_name="Pitch List Generator")
    df = pd.DataFrame(data, columns= ['Markdown'])
    mdString = df.to_string(index=False,header=False)

    html = open("index.html", "w")

    html.write("""<!DOCTYPE html>
    <html lang="en">
            <head>
                <link rel="stylesheet" type="text/css" href="main.css">
            </head>
            <body>
                    <header>
                        <h1>One-Stop Tabletop One-Shot Shop</h1>
                        <p class="subtitle"><i>Ed's one-shot idea storage</i></p>
                    </header>
                    <main>
                        <table style="width:80%">
                            <tr>
                                <th>Markdown:</th>
                                <th>Preview:</th>
                            </tr>
                            <tr>
                                <td class="md">""" + mdString.replace("@","").replace("\n","<br>") + """</td>
                                <td class="rich">""" + convertToRichText(mdString) + """</td>
                            </tr>
                        </table>
                    </main>
                    <footer></footer>
            </body>
    </html>""")

    html.close()

if __name__ == "__main__":
    main()

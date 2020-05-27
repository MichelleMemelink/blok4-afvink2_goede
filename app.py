from flask import Flask, render_template, request
import eiwit

app = Flask(__name__)


@app.route('/', methods=["get"])
def omzetten_naar_eiwit():
    """"de ingevulde DNA sequentie wordt via de functie eiwit.eiwit_maken() omgezet in een
    eiwit sequentie en weergegeven op de html pagina.
    :param: sequentie die in de html pagina wordt ingevuld
    :return: eiwit sequentie die vervolgens op de html pagina wordt weergegeven
    """
    sequentie = request.args.get("sequentie", "")
    return render_template('afvinkopdracht2.html', seq_eiwit=eiwit.eiwit_maken(sequentie))


if __name__ == '__main__':
    app.run()

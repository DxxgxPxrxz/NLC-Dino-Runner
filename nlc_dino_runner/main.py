#EL ARCHIVO MAIN SE VA A ENCARGAR DE CORRER EL JUEGO


from nlc_dino_runner.components.game import Game #Importando una class desde un Python File proveniente de la carpeta COMPONENTS (en este caso la class llamada "Game")

if __name__ == "__main__": #El __name__ se convierte en __main__ mientras el archivo principal es ejecutado
    game = Game() #Definiendo la var game como objeto, con la class importada Game, para correr el juego
    game.execute() 
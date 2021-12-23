from random import choice, randint

EXCUSES = [
    f"Fa {randint(2,30)} anys plovia",
    f"Tinc hora a la pelu, que només hi vaig {randint(1,20)} cops per setmana",
    f"Vaig al gym, la idea és anar-hi {randint(1,20)} cops per setmana",
    "Aquest dia justament vaig a donar sang",
    "Casum l'olla! Tinc un dinar familiar",
    "Demà haig d'anar a passar la itv",
    "El metge m'ha dit que no puc menjar aliments rics en sodi",
    "És que em guardo dies de vacances",
    "És que se m'ha punxat la roda de la bici estàtica i l'he de canviar",
    "És que vai demanar un paquet i crec que m'arribarà llavors",
    "És que fa molt de sol i no tinc crema",
    "És que he d'anar a treure la marmota a passejar",
    "Estic esperant a que el Jefe em doni el contracte que m'ha dit que ara me'l porta",
    "Estic esperant la corda i tamboret que m'he demanat a amazon",
    "He quedat per fer una muntanya",
    "Jo vindria, però és que se m'ha espatllat el GPS del mòbil",
    "Jo vindria, però m'agrada fer motos",
    "Jo vindria, però és que s'em morirà el peix que vaig a comprar ara",
    "Justament aquest dia he quedat per jugar a arrancar cebes",
    "M'he endescuidat de regar el cactus de Gisce",
    "Mha semblat veure una gota a la carretera",
    "No puc venir pk la dona m'ha dit que anes a la platja de palafrugell i em quedés un parell d'hores sota l'aigua",
    "No puc venir que he d'afegir excuses de moto al bot",
    "Plou i fa sol, em quedo a casa sol",
    "Se m'ha mort el PC i li fem un funeral. Tenia una 3080ti",
    "Se m'ha mort la PS5 i li fem un funeral. Poques que n'hi han...",
    "Soc un mort de gana",
    "Tinc el rellotge en format 24h",
    "Tinc un conegut que fa casi un any que no veig que té corona, així que faig quarentena per si de cas.",
    "Tu que m'acaben de trucar que d'aqui 20min anem a fer una implantació i no sé quan tornaré.",
    "Volia venir pro no soy 1000itar",
    "Volia venir pro no soy 1000itante",
    "Volia venir pro no soy 100tifiko",
    "Ho sento sóc simracer",
    "He d'anar a agafar l'AVE",
    "M'he equivocat i he anat al Pagès Original",
    "Sóc vegetarià i fan tapes amb carn",
    f"Estic en remot i visc {randint(1,50)} km lluny",
    "M'estic preparant pel proper canvi de tarifes",
    "Treballo als Països Baixos",
    "He quedat per anar al cine, la peli es diu 'No tinc ganes de venir'. Diuen que és molt bona!",
    f"Haig d'anar a plantar {randint(1,50)} regues de cebes, {randint(1,50)} de cols, {randint(1,50)} d'alls i {randint(1,50)} de brocolis",
    "Tinc un problema i no puc venir",
    "Es que he anat a donar sang i no m'arrba al creelllkakakak",
    f"Ara acabo de recordar que vaig al rocodrom, intento anar {randint(1,50)} vegades per setmana",
    "Brumm brummmmm",
    "Vindria però no bec cervesa",
    "No puc venir perque m'agrada anar per l'autopista, ara que son gratuites"
    "He d'anar a casa a simular indexades",
    "El meu horòscop em diu que he de menjar 44 peces de fruita diàries i avui vaig tard",
    "No puc deixar sola la serp que tinc a casa o es menjarà el hàmster",
    "Començo un curs de ganxet a Udemy i em fa molta il·lusió",
    "He llegit a Twitter que avui tinc que holdear BTC",
    "Tinc que anar a posar pinso a les gallines. No obren fins dilluns que ve",
    "He tingut que marxar de la ciutat per un temps i no sé quan podré tornar. M'han dit que millor no expliqui perquè."
    "M'han detingut per no recollir una caca de gos. Envia 2.000€ a freemortdegana.com per treure'm d'aquí.",
    "M'he comprat un yo-yo i estic recuperant la meva infància. Seré al parc de sota de casa, berenant pa amb xocolata",
    "M'encantaria, però no em ve de gust",
    "La meva religió no em permet quedar avui amb persones que tinguin noms que continguin vocals. Vinc a la propera!",
    "És que fa temps que estic enfadat amb vosaltres i no recordo perquè. No us vull veure fins que s'em passi.",
    "Uff, impossible. Just tenia pensat trucar a Movistar per a donar-me de baixa. Us veig l'any que ve.",
    "Quan acabi amb les excuses del bot, n'he d'afegir també a unes declaracions del Rajoy. A veure si colen!",
    "Mmm... no sé si arribaria a temps. Estic esperant que acabi la sèrie One Piece. Després estaré disponible."
]


def get_random_excuse() -> str:
    """Generate a random text for motos

    Returns:
        str: Moto quote
    """
    return choice(EXCUSES)

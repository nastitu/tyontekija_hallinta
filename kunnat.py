from ohjelma.models import Kunta

# Kuntien lisääminen
kunnat = [
    ('ahvenanmaa', ['Maarianhamina', 'Jomala', 'Föglö', 'Kumlinge']),
    ('etela_karjala', ['Lappeenranta', 'Imatra', 'Parikkala', 'Rautjärvi']),
    ('etela_pohjanmaa', ['Seinäjoki', 'Lapua', 'Alajärvi', 'Alavus']),
    ('etela_savo', ['Savonlinna', 'Mikkeli', 'Pieksämäki', 'Juva']),
    ('kainuu', ['Kajaani', 'Sotkamo', 'Kuhmo', 'Paltamo']),
    ('kanta_hame', ['Hämeenlinna', 'Riihimäki', 'Forssa', 'Janakkala']),
    ('keski_pohjanmaa', ['Kokkola', 'Kannus', 'Kaustinen', 'Veteli']),
    ('keski_suomi', ['Jyväskylä', 'Jämsä', 'Äänekoski', 'Saarijärvi']),
    ('kymenlaakso', ['Kotka', 'Kouvola', 'Hamina', 'Pyhtää']),
    ('lappi', ['Rovaniemi', 'Kemi', 'Tornio', 'Kemijärvi']),
    ('pirkanmaa', ['Tampere', 'Nokia', 'Ylöjärvi', 'Sastamala']),
    ('pohjanmaa', ['Vaasa', 'Pietarsaari', 'Kristiinankaupunki', 'Kaskinen']),
    ('pohjois_karjala', ['Joensuu', 'Lieksa', 'Nurmes', 'Kitee']),
    ('pohjois_pohjanmaa', ['Oulu', 'Kuusamo', 'Raahe', 'Kalajoki']),
    ('pohjois_savo', ['Kuopio', 'Iisalmi', 'Varkaus', 'Siilinjärvi']),
    ('paijat_hame', ['Lahti', 'Heinola', 'Orimattila', 'Hollola']),
    ('satakunta', ['Pori', 'Rauma', 'Harjavalta', 'Huittinen']),
    ('uusimaa', ['Helsinki', 'Espoo', 'Vantaa', 'Porvoo']),
    ('varsinais_suomi', ['Turku', 'Salo', 'Kaarina', 'Naantali']),
]

for maakunta, kunnat_list in kunnat:
    for kunta in kunnat_list:
        Kunta.objects.create(nimi=kunta, maakunta=maakunta)

print("Kunnat lisätty onnistuneesti!")

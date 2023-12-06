from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from marvel.serializers import LoginRequestSerializer
import json

class Login(APIView):
    def post(self, request, format=None):
        serializer = LoginRequestSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.data["username"] == "admin" and serializer.data["password"] == "123456":
                return Response({"status": "success", "code": 200, "data": {"id":"007", "username": "bond-james", "firstname": "james", "lastname": "bond"} }, status=status.HTTP_200_OK, content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Places(APIView):
    def get(self, request):
        sites = """
        [
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Tallin",
  "Latitud": 59.4376603802048,
  "Longitud": 24.7453292264818,
  "Monumento": "Raekoja plats",
  "Descripcion": "Raekoja plats, or Town Hall Square, is a historic town square located in the center of Tallinns Old Town. Adjacent to the Tallinn Town Hall, this picturesque square is a vibrant hub of activity. It serves as a venue for various festivals, concerts, and cultural events, including the popular Tallinn Old Town Days. The square is surrounded by charming bars and restaurants, offering a variety of dining options. Additionally, it hosts a regular market where visitors can find traditional Estonian items and souvenirs. Dont miss the opportunity to visit the historic Raeapteek, one of Europes oldest continuously operating pharmacies, which has been in business since the 15th century. With its rich history and lively atmosphere, Raekoja plats is a mustvisit destination in Tallinn.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/raekoja%20plats.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4370082855798,
  "Longitud": 24.7453168281722,
  "Monumento": "Tallinn Town Hall",
  "Descripcion": "Welcome to Tallinn Town Hall (Raekoda), the oldest town hall in the Baltic Sea region and Scandinavia. This remarkable Gothic building is located in Tallinns Old Town, next to the bustling Town Hall Square. Admire the impressive exterior, with its crenelated battlements, dragon headshaped gargoyles, and the iconic weather vane Old Thomas atop the spire. Step inside to explore the historic chambers, including the town hall writers room, the town hall meetings room, and the citizens hall. From the top of the tower, enjoy panoramic views of the city. Tallinn Town Hall is not only a symbol of governance but also a concert venue and museum, offering insights into the citys historical and architectural heritage. Discover the centurieslong history and beauty of Tallinn at this iconic landmark.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/tailinn%20town%20hall.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4357832766935,
  "Longitud": 24.7389936746626,
  "Monumento": "Alexander Nevsky Cathedral, Tallin",
  "Descripcion": "The Alexander Nevsky Cathedral, located on Toompea Hill in central Tallinn, Estonia, is a magnificent orthodox cathedral built in the Russian Revival style. Constructed between 1894 and 1900, the cathedral stands as a symbol of the countrys history during its time as part of the Russian Empire. With its impressive cupolas, it is the largest orthodox church in Tallinn. Dedicated to Alexander Nevsky, the grand prince of Kiev and a revered saint, the cathedral commemorates his victory in the Battle of the Ice. The interior of the cathedral is adorned with exquisite decorations, including three gilded wooden iconostases and stunning stained glass windows. The cathedrals survival is a testament to its resilience, having undergone meticulous restoration after the Soviet occupation ended in 1991.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/alexander%20nevsky%20cathedral.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4358247310703,
  "Longitud": 24.7372222264768,
  "Monumento": "Toompea Castle",
  "Descripcion": "Toompea Castle, located on Toompea Hill in Tallinn, is a medieval fortress that now serves as the Parliament of Estonia. Its origins date back to the 9th century AD, and it has since witnessed various rulers and architectural transformations. The castle was initially a stronghold of the ancient Estonians and was later taken over by Danish crusaders in 1219. It became known as the Castle of the Danes and played a significant role in the history of Tallinn. Over the centuries, it passed through the hands of different orders and powers, including the Teutonic Order and Sweden. In the 18th century, the castle underwent major renovations, acquiring Baroque and Neoclassical elements. Today, it stands as a symbol of Estonias political power and is a fascinating site to explore.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/toompea%20castle.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4378366995985,
  "Longitud": 24.7451465069437,
  "Monumento": "Tallinn Old Town",
  "Descripcion": "Welcome to Tallinn Old Town, the oldest part of Tallinn, Estonia. With its wellpreserved medieval and Hanseatic architecture, the Old Town takes you back in time to the 13th century. Designated as a UNESCO World Heritage site since 1997, it showcases an exceptional city plan that has endured through the centuries. Enclosed by the Walls of Tallinn, the Old Town covers an area of 113 hectares, with an additional buffer zone of 2,253 hectares.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/talinn%20old%20town.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4413436293202,
  "Longitud": 24.7478066976412,
  "Monumento": "St. Olafs Church",
  "Descripcion": "Welcome to St. Olafs Church, a historic landmark in Tallinn, Estonia. Believed to have been built in the 12th century, this church was once the center of the Scandinavian community before Denmarks conquest of the city. Named after King Olaf II of Norway, also known as St. Olaf, this church holds centuries of history within its walls. Its tower, standing at 124 meters, has undergone multiple reconstructions and restoration throughout the years. It was even the tallest building in the world from 1549 to 1625, reaching a height of 159 meters. Today, the church stands as a symbol of resilience and faith. Explore its rich history and admire the stunning architecture as you step into the past.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/st.%20olaf%E2%80%99s%20church.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4385350500336,
  "Longitud": 24.791184297064,
  "Monumento": "Kadriorg Palace",
  "Descripcion": "Welcome to Kadriorg Palace, a splendid Petrine Baroque masterpiece located in the heart of Tallinn, Estonia. Built between 1718 and 1725, the palace was a gift from Czar Peter the Great to his wife Catherine. Today, it houses the Kadriorg Art Museum, where you can explore a remarkable collection of foreign art spanning from the 16th to the 20th centuries. Admire the grandeur of the palaces architecture, stroll through the picturesque Kadriorg Park, and immerse yourself in the artistic treasures within the museums walls. Discover works by renowned artists such as Jacob Jordaens, Bernardo Strozzi, Ilya Repin, and many more. Kadriorg Palace is a cultural gem that invites you to delve into Estonias rich artistic heritage.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/kadriorg%20palace.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4376935953474,
  "Longitud": 24.7900917536193,
  "Monumento": "Kadriorg Park",
  "Descripcion": "Welcome to Kadriorg Park, a serene oasis in Tallinn that beckons you to immerse yourself in its natural beauty. Established in the early 18th century, the park was part of the summer estate purchased by Peter I. Bordered by Tallinn Bay and the Lasnamäe district, Kadriorg Park spans over one hundred hectares of picturesque landscape. Designed by architect Niccolò Michetti, the park draws inspiration from Italian villas, featuring carefully planned gardens and charming pathways. Take a leisurely stroll amidst the lush greenery, discover hidden corners, and enjoy the tranquil atmosphere. Kadriorg Park is a haven of relaxation and a perfect escape from the bustling city.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/kadriorg%20park.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.471238837861,
  "Longitud": 24.8874166861474,
  "Monumento": "Tallinn TV Tower",
  "Descripcion": "Welcome to the Tallinn TV Tower, a magnificent structure standing at a height of 314 meters in the Pirita district of Tallinn. As a member of the World Federation of Great Towers, it offers breathtaking views from its observation deck. Built in preparation for the 1980 Moscow Summer Olympics, the tower has become an iconic landmark of the city. The architects, David Bassiladze and Yuri Sinis, designed a reinforced concrete base with a steel antenna, allowing for the installation of equipment and a highspeed elevator. The museum showcases the towers construction and offers a glimpse into the world of broadcasting. Experience the thrill of ascending to the top and witnessing panoramic vistas of Tallinn and beyond.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/tailinn%20tv%20tower.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4315052853788,
  "Longitud": 24.6381687613555,
  "Monumento": "Estonian Open Air Museum",
  "Descripcion": "Discover the charm of Estonias rural past at the Estonian Open Air Museum. Situated on a vast 72.22hectare territory, the museum showcases nearly 80 buildings that bring to life the countrys 18th20th century rural architecture and village life. Explore the 14 farms, including a church, inn, schoolhouse, mills, and more, providing a glimpse into different strata of society. Immerse yourself in the authentic atmosphere as you wander through the museums grounds. Dont miss the opportunity to indulge in traditional Estonian dishes at the inn, try your hand at handicrafts, and even enjoy horseback riding. The Estonian Open Air Museum offers a yearround experience, providing workshops, events, and entertainment for visitors of all ages. Only a 15minute drive from the center of Tallinn, this museum is a mustvisit destination.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/estonian%20open%20air%20museum.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4517550523043,
  "Longitud": 24.73835243997,
  "Monumento": "Seaplane Harbour",
  "Descripcion": "Discover the fascinating Lennusadam, a port located by Tallinn Bay in Estonia. The highlight of this maritime site is its remarkable seaplane hangar, a historical monument of international importance. Today, it serves as a branch of the Estonian Maritime Museum. Explore the exhibition area of over 5,000 square meters, featuring more than 200 lifesize maritime and military history exhibits. Marvel at the unique seaplanes, navigational aids, naval weapons, and coastal defense displays. Dont miss the centerpiece of the hangar, the only preserved submarine Lembit in Estonia. Immerse yourself in the captivating stories of naval warfare and maritime history as you delve into the seven themed sections. The Lennusadam is a mustvisit for history enthusiasts and those interested in Estonias rich maritime heritage.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/seaplane%20harbour.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4386907732798,
  "Longitud": 24.7481736592668,
  "Monumento": "Tallinn City Museum",
  "Descripcion": "The Tallinn City Museum, located at Rusen 17, presents a comprehensive exhibition showcasing the history of Tallinn from ancient times to Estonias reindependence. Visitors can explore five floors of captivating displays. A unique feature of the museum is the faience and porcelain open storage, housing a collection of nearly 2,000 sets from Estonia, Europe, China, and Japan. The museum has transformed its cellars into an exhibition space, offering a glimpse into hidden treasures such as pottery, copper, brass, and pewter objects. The museum also showcases a collection of 19thcentury views, including works by renowned artists like Karl Ferdinand von Kügelgen. It provides a fascinating perspective on Tallinns past before the era of railways and urbanization. Join a journey through Tallinns history at the Tallinn City Museum.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/taillinn%20city%20museum.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4425275558023,
  "Longitud": 24.7494852527159,
  "Monumento": "Tallinn Maritime Museum",
  "Descripcion": "Discover the rich maritime heritage of Tallinn at the Estonian Maritime Museum. Founded in 1935, the museum is dedicated to showcasing maritime exhibits, conducting scientific research, and exploring underwater archaeology. The main expositions are located in Tallinns Paksu Margareeta and Lennusadama. At the museum, visitors can explore the captivating history of seafaring through engaging exhibits. The renovated Paksu Margareeta, completed in 2019, offers a glimpse into the maritime past, while the Tallinn seaplane hangar, opened in 2012, showcases the museums modern and popular displays. With plans to expand to Naissaar, the Estonian Maritime Museum continues to provide a fascinating journey into the maritime world, capturing the essence of Tallinns coastal heritage.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/taillinn%20maritime%20museum.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.420205582353,
  "Longitud": 24.6597376237609,
  "Monumento": "Tallinn Zoo",
  "Descripcion": "Explore Tallin Zoo, the only zoo in Estonia. Established in 1939, it is home to a diverse collection of 13,336 animals representing 548 species. Discover the worlds largest mountain goat and sheep collection, two tropical houses with reptiles, exotic birds, and primates, and the Elephant House featuring African elephants and rhinos. Visit the Alpinarium to see snow leopards and mountain sheep. Marvel at the Hawk Mountain, home to eagles and owls. The zoo actively participates in conservation and breeding programs for endangered species such as the Amur leopard and black rhinoceros. Dont miss the ongoing modernization efforts, with new exhibits planned for bears, wolves, tigers, and more. Enjoy a day surrounded by fascinating wildlife at Tallin Zoo.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/taillinn%20zoo.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4362283413091,
  "Longitud": 24.7961043860008,
  "Monumento": "Kumu Art Museum",
  "Descripcion": "Discover the Kumu Art Museum, one of Estonias largest art museums and a prominent cultural hub. Located in Tallinn, it showcases both permanent collections and temporary exhibitions, including Estonian art from the 18th century to the present day. Marvel at the works of renowned artists, from Socialist realism to contemporary expressions. Designed by Finnish architect Pekka Vapaavuori, the museum seamlessly blends into the picturesque Kadriorg park. Explore the various floors, each dedicated to a different period in Estonian art history. Take in the beauty of the restored Kadriorg Palace, now a branch of the museum housing a remarkable foreign art collection. Dont miss the recognition received by Kumu, such as the European Museum of the Year Award in 2008. Immerse yourself in the world of art at Kumu Art Museum.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/kumu%20art%20museum.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4384086276751,
  "Longitud": 24.7449810566402,
  "Monumento": "Estonian History Museum",
  "Descripcion": "The Estonian History Museum in Tallinn offers a captivating exploration of Estonias history. Established in 1987, it focuses on the significant political and social changes of the twentieth century. Through historically dressed mannequins and recreated domestic interiors, visitors gain insight into different time periods. The exhibits include army uniforms and weapons from the 1940s and 1950s, as well as original artifacts like the Forest Brothers hut. With four locations  Maarjamäe Palace, the Great Guild hall, the Film Museum, and the Theatre and Music Museum  the museum offers a multifaceted experience.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/estonian%20history%20museum.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4345010301994,
  "Longitud": 24.7501015730369,
  "Monumento": "Estonian National Opera",
  "Descripcion": "The Estonian National Opera, based at the Estonia Theatre in Tallinn, is the national opera company of Estonia. With a rich history dating back to 1870, the opera company offers a vibrant and diverse season of operas, ballets, and operettas/musicals. The Estonia Theatre, also known as the Estonia Opera House, has been a cultural landmark since its opening in 1913. Despite enduring damage during World War II, it was rebuilt and reopened in 1947. The theatre is renowned for its beautiful interior, featuring the ceiling painted in the style of Socialist Realism by esteemed Estonian painters. Today, the Estonian National Opera continues to captivate audiences with its exceptional performances and remains an integral part of Estonias vibrant arts scene.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/estonian%20national%20opera.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4393750018606,
  "Longitud": 24.7422676498184,
  "Monumento": "Sauna Tower",
  "Descripcion": "Welcome to the Sauna Tower, a fascinating piece of Tallinns medieval history. Located on the northeastern side of the city wall, this defense tower was originally part of the St. Michaels monastery sauna. Built in 13711372, it underwent several renovations and modernizations over the centuries. The tower reached a height of 12 meters in the 15th century, and although the top was demolished in the 19th century, it was reconstructed in 1898 based on the Nunnadetagus tower. In 2004, extensive conservation and restoration works were carried out on the Sauna Tower, along with the Nun Tower and Kuldjala Tower. Today, these towers and the section of the city wall between them are owned by the Tallinn Cultural Heritage Agency.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/sauna%20tower.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.471378578023,
  "Longitud": 24.8801886655504,
  "Monumento": "Tallinn Botanic Garden",
  "Descripcion": "Tallinn Botanic Garden is the largest botanical garden in Estonia, spanning an impressive area of 123 hectares. Established in 1961 under the Academy of Sciences of the Estonian SSR, it serves as a hub for research, conservation, and public engagement. The garden features a diverse range of plant collections, including both indigenous species and carefully acclimatized foreign plants. Visitors can explore the openair collections, which were opened to the public in 1970, and the greenhouse collections, accessible since 1971. With its rich history and commitment to botanical research and preservation, Tallinn Botanic Garden is a cherished destination for nature enthusiasts, horticulturists, and researchers alike.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/talinn%20botanic%20garden.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4445663492458,
  "Longitud": 24.8072686980694,
  "Monumento": "Tallinn Song Festival Grounds",
  "Descripcion": "The Tallinn Song Festival Grounds, known as Lauluväljak, host the Estonian Song Festival every five years. Established in 1869 by Johann Voldemar Jannsen, the festival played a crucial role in fostering Estonias national awakening. The current stage, designed by Karl Burman, was built in 1928 to accommodate 15,000 performers. In 1959, a larger arched stage was constructed by architect Henno Sepmann for the 20th anniversary of the Estonian SSR. This iconic stage, capable of holding over 15,000 singers, witnessed the historic 1960 Estonian Song Festival. The grounds gained global recognition during the Singing Revolution in 1988, contributing to the overthrow of Soviet rule. Today, the venue also hosts international acts and concerts, attracting renowned artists and large crowds.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/tallinn%20song%20festival%20grounds.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4376144553584,
  "Longitud": 24.7486726179613,
  "Monumento": "St. Catherines Passage",
  "Descripcion": "Catherines Alley, formerly known as Monks Alley, is a charming pathway in Tallinn, Estonia. It stretches from Vene Street to Müürivahe Street, passing the southern end of the Dominican monastery. The alley takes its name from St. Catherines church, believed to have been constructed over 700 years ago. On the southern side of the alley, youll find a collection of buildings primarily dating back to the 15th to 17th centuries. Catherines Alley retains its medieval allure and underwent restoration in 1995. Today, it is home to various handicraft workshops where visitors can witness artisans at work, crafting ceramics, hats, glass, and more. Immerse yourself in the ambiance of this historical and artistic enclave as you explore Catherines Alley.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/sta.%20catherine%E2%80%99s%20passage.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4365627611686,
  "Longitud": 24.7501056791545,
  "Monumento": "Viru Gate",
  "Descripcion": "Discover the historic Barbican Viru Gate in Tallinn, Estonia. This 14thcentury defense structure is part of the citys renowned city walls. The gate, with its preserved corner towers, invites you to step back in time. Experience the vibrant atmosphere of Viru Street, a bustling pedestrian street lined with shops and restaurants, making it a popular destination in the Old Town. Immerse yourself in the rich heritage of Tallinn as you explore this captivating gateway to history.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/viru%20gate.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4375206235411,
  "Longitud": 24.7496594882386,
  "Monumento": "Hellemann Tower and Town Wall Walkway",
  "Descripcion": "Hellemann Tower, part of Tallinns medieval defense structures, stands as a significant landmark in the Old Town. Located on Müürivahe Street 48/Uus Street 1, it is adjacent to the Viru Gate and the Munkadetagune Tower. Originally constructed as a defensive fortification, the tower served various purposes over the years, including being owned by the Cinema Union during the Soviet era. Today, the tower has undergone thorough restoration, including the restoration of the defense passage that connects it to the Munkadetagune Tower. Visitors can explore this historic site and walk through the nearly 200meter defense passage, providing a unique glimpse into Tallinns medieval past.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/hellemann%20tower%20and%20town%20hall%20walkway.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4356574689516,
  "Longitud": 24.7407009779025,
  "Monumento": "Stable Tower and Town Wall Walkway",
  "Descripcion": "The Tall Tower, situated on the southwestern section of the Tallinn city wall, is a remarkable structure between the Maiden Tower and the Short Leg Gate. As one of the few cantilever towers known as echogett, it rests on a protruding beam. Originally used as a watchtower, it features viewing and shooting holes, along with pitch knobs for defense. The tower acquired its name from the adjacent Marstall yard, where cannons, church bells, and horse stables were once located. Throughout its history, the tower endured damage and collapse, serving as a prison in the 17th century. In the 20th century, a passage was created through the city wall, connecting Toompea to the Danish Kings Garden. Today, visitors can explore the tower by visiting the Kiek in de Kök Fortification Museum.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/stable%20tower%20and%20town%20hall%20walkway.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4347015027208,
  "Longitud": 24.7411906119491,
  "Monumento": "Kiek in de Kök Museum and Bastion Tunnels",
  "Descripcion": "Kiek in de Kök Museum and Bastion Tunnels, located in Tallinn, Estonia, offer a captivating journey into the citys medieval past. The Kiek in de Kök Tower, originally built in the 15th century, stands as a towering symbol of Tallinns fortifications. Its name, meaning peek into the kitchen in Low German, reflects its strategic position for observing enemies. The tower was extensively rebuilt over the years and now houses the Tallinn City Museum. Visitors can explore the museums exhibitions, which showcase the citys history and provide insights into its defensive systems. Adjacent to the tower, the Bastion Tunnels offer a fascinating underground network of passages. Renovated in recent years, the tunnels connect the Kiek in de Kök Tower to the Inger and Swedish Bastions. Exploring these historic tunnels provides a unique perspective on the citys defenses and offers a memorable experience.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/kiek%20in%20de%20k%C3%B6k%20museum%20and%20bastol%20tunnels.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4425299636093,
  "Longitud": 24.7491362333198,
  "Monumento": "Great Coastal Gate and Fat Margaret Tower",
  "Descripcion": "The Great Coastal Gate, also known as Suur Rannavärav in Estonian, dates back to the 14th century. It was originally constructed to protect the harbor and underwent significant expansion and additions in the 16th century. The most notable addition was the Fat Margaret Tower, which served as an artillery tower. With a diameter of 25 meters and a unique threequarter circle shape, the tower featured thick walls and wooden beam ceilings. Over the years, the complex underwent various reconstructions and adaptations. In the 19th century, Fat Margaret was repurposed as a prison, and later it became the premises of the City Museum. Today, the Great Coastal Gate and Fat Margaret Tower house the Estonian Maritime Museum, showcasing the rich maritime history of Tallinn and offering visitors a chance to explore the intriguing past of this iconic landmark.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/great%20coastal%20gate%20and%20fat%20margaret%20tower.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.437676121542,
  "Longitud": 24.7427024940218,
  "Monumento": "Long Leg Gate Tower",
  "Descripcion": "The Long Leg Gate Tower, also known as Pika jala gate tower, is a defense tower situated in Tallinns old town. Built in the late 17th century, it likely stands on the site of an earlier wooden gate. The tower is located at the intersection of Pika jala, Rataskaevu, and Nunne streets.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/long%20leg%20great%20tower.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4351399513289,
  "Longitud": 24.7367907222115,
  "Monumento": "Pikk Hermann Tower",
  "Descripcion": "Pikk Hermann, also known as Tall Hermann or Langer Hermann, is a tower located on Toompea hill in Tallinn, Estonia. Built in the 14th century and later reconstructed in the 16th century, the tower stands at a height of 45.6 meters (150 ft). With its 215step staircase, Pikk Hermann offers visitors access to ten internal floors and a viewing platform at the top. Adjacent to the Estonian Parliament building, the towers most prominent feature is the flag that flies at its peak, serving as a symbol of the current government. On February 24, 1989, the blueblackwhite flag of Estonia was raised atop Pikk Hermann, marking a significant moment in the countrys history.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/pikk%20hermann%20tower.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Pirita",
  "Latitud": 59.4533735084343,
  "Longitud": 24.8121981400839,
  "Monumento": "Tallin Film Museum",
  "Descripcion": "The Film Museum in Tallinn offers a captivating exploration of Estonian cinema and the filmmaking process. Through its exhibition Take One, visitors can delve into the rich history of Estonian film and discover the behindthescenes world of moviemaking. With interactive elements, such as green screen experiences, visitors can even step into the frame and experience the magic of film firsthand. The museum also houses a modern cinema for film screenings and hosts temporary exhibitions on various filmrelated subjects. As part of the Estonian History Museum, the Film Museum preserves and presents film heritage, including costumes, props, photographs, and designs. Its unique building in the Maarjamäe Palace complex is a mustvisit destination for film enthusiasts.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/Tallin%20Film%20Museum.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Pirita",
  "Latitud": 59.4524967038824,
  "Longitud": 24.8100789608698,
  "Monumento": "Maarjamäe Palace",
  "Descripcion": "Maarjamäe Palace in Tallinn, Estonia, has a rich history that spans centuries. Initially known as Strietberg, it was a popular summer destination. Over time, it housed a sugar factory and later became a summer manor. In the 1930s, it was transformed into an elegant restauranthotel called RivieraPalais. During various periods, the palace served as a military aviation school and Soviet Army quarters. Extensive renovations took place in the 1980s, restoring the palaces external appearance and creating exhibition spaces. Today, Maarjamäe Palace is part of the Estonian History Museum and serves as a history discovery center. Visitors can explore the interactive exhibition My Free Country, which chronicles Estonias past and future. The palace is also home to the Estonian Film Museum, and the surrounding park offers recreational areas and outdoor exhibitions.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/Maarjam%C3%A4e%20Palace.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Pirita",
  "Latitud": 59.4384489850103,
  "Longitud": 24.744976455313,
  "Monumento": "Tallin Great Guild Hall",
  "Descripcion": "The Great Guild Hall in Tallinn is a notable medieval public building. Completed in 1410, this Gothicstyle structure was commissioned by the Great Guild, an association of Hanseatic merchants. Throughout history, it has hosted a wide range of events, from lavish parties to church services and court proceedings. In the Middle Ages, the cellar stored wine, and in the 19th and 20th centuries, it operated as a popular wine cellar called Das Süsse Loch (Sweet Hole). Since 1952, the Estonian History Museum has been located in the Great Guild Hall. In 20102011, the building underwent extensive restoration and refurbishment, supported by the European Regional Development Fund and the Estonian Ministry of Culture. The interior design and new permanent exhibition were collaborative efforts involving the Estonian History Museum, OÜ KOKO Arhitektid, and OÜ Produktsioonigrupp. The Great Guild Hall holds significant historical importance as it reflects the trade and cultural developments of medieval northern Europe. In recognition of its significance, it was awarded the European Heritage Label in 2013.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/Tallin Great Guild Hall.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4338537543923,
  "Longitud": 24.7442505841487,
  "Monumento": "Freedom Square",
  "Descripcion": "Freedom Square, located at the southern end of Tallinns Old Town, serves as a gathering place for state functions and concerts. Bounded by St. Johns Church, Kaarli Boulevard, and a Victory Column commemorating the Estonian War of Independence, the square underwent a transformation from a parking lot to a vibrant plaza. Designed by architects Tiit Trummal, Veljo Kaasik, and Andres Alver, it spans an area of 7,752 m2, with dimensions of approximately 110 m by 75 m. The square holds historical significance, having been the site of the former Swedish bastion and later hosting a monument to Peter I. Today, it stands as a symbol of freedom and remembrance, with the Cross of Liberty and the Monument to the War of Independence paying tribute to those who sacrificed for Estonias independence.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/Freedom%20Square.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4356958188933,
  "Longitud": 24.7410654148368,
  "Monumento": "Danish Kings Garden",
  "Descripcion": "The Danish Kings Garden is a green area in Tallinns Old Town, located west of Rüütli Street. It is named after the Danish king Valdemar II, whose victory in 1219 led to Danish rule in Tallinn for over a hundred years. Legends suggest that the Danish flag, Dannebrog, was obtained by the Danes in this very place during a battle on Toompea Hill. The garden is adorned with a stone memorial plaque dedicated to artists Paul and Kristjan Raua. It serves as a serene retreat and hosts the annual Dannebrog Day celebration, commemorating the historic ties between Denmark and Estonia.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/Danish%20Kings%20Garden.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.435987883004,
  "Longitud": 24.7427981274754,
  "Monumento": "Saint Nicolas Church and Museum",
  "Descripcion": "St. Nicholas Church, founded in the 13th century, was a prominent parish church in medieval Tallinn. Dedicated to St. Nicholas, the patron saint of merchants and seafarers, it was known for its wealth. The church underwent various expansions and renovations over the centuries, including the addition of chapels and the rebuilding of the chancel and nave. St. Nicholas Church housed numerous side altars and valuable works of art, such as Bernt Notkes Dance of Death and the magnificent retable of the high altar from the workshop of Hermen Rode. With the arrival of the Reformation, the church became a Lutheran congregation and underwent further modifications to accommodate the new faith. Epitaphs and memorial chapels were added to honor notable individuals. The Chapel of St. George was eventually transformed into the North Hall.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/Saint%20Nicolas%20Church%20and%20Museum.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.438588437705,
  "Longitud": 24.7409295442067,
  "Monumento": "Patkuli viewing platform",
  "Descripcion": "The Patkuli viewing platform, located in the historic district of Tallinn, offers a picturesque and captivating view of the Old Town, its towers, and walls, extending all the way to the port. Builtin 1903, the stairway leading to the platform consists of 157 steps, connecting Toompea Hill to the lower town. The stairway emerges near Snelli Pond in Toompark, providing a convenient access point.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/Patkuli%20viewing%20platform.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.437106333684,
  "Longitud": 24.7399826005883,
  "Monumento": "Estonian Knighthood House",
  "Descripcion": "The Estonian Knighthood House, located in Toompea, Tallinns historic inner town, is a notable building with a rich history. It served as the meeting place for the German nobles of the Estonian Knighthood, who held power in Estonia for centuries. The current Renaissance Revivalstyle building, designed by architect Georg Winterhalter and constructed between 1845 and 1848, is the fourth Knighthood House. After Estonia gained independence in 1920, the building was repurposed as the Ministry of Foreign Affairs. It later served as the National Library of Estonia from 1948 to 1992. In 1993, part of the art collection from Kadriorg Palace found a home in the Estonian Knighthood House. Today, the building houses the Estonian Academy of Arts, although it is slated to relocate in 2016.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/Estonian%20Knighthood%20House.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4373935834165,
  "Longitud": 24.7376972418277,
  "Monumento": "Piiskopi viewing platform",
  "Descripcion": "The Piiskopi observation platform, situated on the western side of Toompea, provides a picturesque view of the Pelgulinna and Kalamaja districts. Also known as the Bishops Garden, this charming square offers a hidden retreat. During the renovation, the medieval well was restored, and the garden was adorned with paradise apple trees. Additionally, visitors can marvel at the presence of the two oldest oak trees in Toompea.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/Piiskopi%20viewing%20platform.jpg"
 },
 {
  "Pais": "Estonia",
  "Ciudad": "Tallin",
  "Distrito": "Vanalinn",
  "Latitud": 59.4377381708966,
  "Longitud": 24.7420733016788,
  "Monumento": "Kohtuotsa viewing platform",
  "Descripcion": "The Kohtuotsa viewing platform, located on the northern side of Toompea hill, offers breathtaking vistas of Tallinns Old Town with its iconic red roofs and majestic spires. From this vantage point, visitors can also marvel at the modern highrise buildings in the new part of the city, creating a striking contrast. In the distance, the Gulf of Finland, the bustling port, and the picturesque Pirita district complete the panoramic view. Please note that the platform is currently closed for renovation and is scheduled to reopen in October 2022.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tallinn/Kohtuotsa%20viewing%20platform.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Barranco",
  "Latitud": 12.1489255288097,
  "Longitud": 77.0222811339171,
  "Monumento": "Puente de los suspiros",
  "Descripcion": "The Bridge of Sighs is a beautiful landmark located in the Barranco district of Lima, Peru. Built in the late 19th century, its a popular spot for photography, with its picturesque location overlooking the Pacific Ocean.Legend has it that the bridge gets its name from the sighs of young lovers who would cross it and make a wish. Its also a popular source of inspiration for artists and writers, including the famous Peruvian author, Mario Vargas Llosa and Chabuca Granda. Located in the heart of Barranco, the Bridge of Sighs is surrounded by a lively arts and culture scene, with numerous galleries, museums, and performance spaces in the area. You can also find a variety of restaurants and cafes serving traditional Peruvian cuisine.Whether youre a lover of history, architecture, or simply looking for a beautiful spot to take in the views, the Bridge of Sighs is a mustsee destination in Lima",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos%20barranco/PUENTE%20DE%20LOS%20SUSPIROS%201.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Barranco",
  "Latitud": 12.147662592426,
  "Longitud": 77.0179799465826,
  "Monumento": "Plaza de Barranco",
  "Descripcion": "The Main Plaza of Barranco is a beautiful and historic square in Limas bohemian district. This charming plaza is home to several cultural attractions, including the Barranco Cathedral and the Barranco Train Station, both of which feature stunning architecture and intricate details.The plaza is also a great place to try traditional Peruvian cuisine or sip on a refreshing pisco sour while enjoying the lively atmosphere and street performers. And if youre looking for souvenirs, you can find a variety of artisanal crafts and textiles at the numerous shops and vendors that line the plaza.Whether youre interested in history, architecture, or simply looking for a vibrant and cultural atmosphere, the Main Plaza of Barranco is a mustsee destination in Lima.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos%20barranco/PLAZA%20PRINCIPAL%202.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Barranco",
  "Latitud": 12.1480190076417,
  "Longitud": 77.0212937117131,
  "Monumento": "Bajada de los banos",
  "Descripcion": "Bajada de los Banos is a colorful street in the bohemian district of Barranco, Lima. Its famous for its street art, trendy cafes, and art galleries, and is a mustvisit destination for anyone exploring the area. Take a leisurely stroll down the street, stopping to admire the artwork and snap a few photos along the way. And for those looking for a bite to eat, there are several restaurants and cafes serving traditional Peruvian cuisine and international dishes.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos%20barranco/BAJADA%20DE%20BA%C3%91OS%201.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Barranco",
  "Latitud": 12.1485255740411,
  "Longitud": 77.0209628743169,
  "Monumento": "Parroquia la Santisima Cruz",
  "Descripcion": "The Cathedral of Barranco, or the Church of La Santísima Cruz, is a beautiful colonialstyle church located in the heart of Barranco. It is known for its stunning architecture and collection of religious artifacts, including statues and paintings of the Virgin Mary and other saints.  The Cathedral of Barranco is also home to a number of interesting events and traditions. One of the most popular is the annual procession of the Holy Cross, which takes place on May 3rd. During the procession, the cross is carried through the streets of Barranco, accompanied by a band playing traditional Peruvian music.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos%20barranco/PARROQUIA%20STA%20CRUZ%201.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Barranco",
  "Latitud": 12.1501133014828,
  "Longitud": 77.0237980039277,
  "Monumento": "Mirador de Barranco",
  "Descripcion": "The Mirador of Barranco is a beautiful viewpoint in Lima, Peru, offering stunning views of the Pacific Ocean and the city. Legend has it that the Mirador was once a popular spot for lovers to meet in secret, and its surrounded by art galleries and cultural centers. One of the most interesting landmarks near the Mirador is the historic Puente de los Suspiros, or the Bridge of Sighs, which is said to have inspired a famous Peruvian song. Whether youre interested in art, history, or simply looking for a beautiful spot to take in the views, the Mirador of Barranco is a mustsee destination.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos%20barranco/MIRADOR%20BARRANCO%202.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Barranco",
  "Latitud": 12.1502953262212,
  "Longitud": 77.0218514626077,
  "Monumento": "Barranco Train Station",
  "Descripcion": "The Old Barranco Train Station is a beloved landmark in Barranco, Lima, Peru. This historic station has been transformed into a cultural center, hosting art exhibits, concerts, and other events.The stations clock tower is a popular spot for photos, offering stunning views of the surrounding area. Legend has it that the tower was the site of a tragic love story between a train conductor and a young woman.Today, the Old Barranco Train Station is a great place to experience the local culture and immerse yourself in the rich history and folklore of Barranco.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos%20barranco/ESTACION%20DEL%20TREN.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Barranco",
  "Latitud": 12.1545703865556,
  "Longitud": 77.0221830743168,
  "Monumento": "Pedro de Osma Museum",
  "Descripcion": "The Pedro de Osma Museum and Palace is a stunning cultural landmark in Barranco, Lima, Peru. Housed in a beautiful 20thcentury palace, the museum features an impressive collection of Peruvian art and artifacts, as well as a tranquil garden and courtyard. Guided tours offer a fascinating insight into Peruvian history and culture. An interesting fact is that the museum was almost destroyed in the 1970s, but was restored to its former glory in the 1990s. A mustvisit destination for art and history lovers, as well as those seeking a peaceful escape in Barranco.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos%20barranco/MUSEO%20PEDRO%20DE%20OSMA%201.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Barranco",
  "Latitud": 12.1494351060709,
  "Longitud": 77.0222944026123,
  "Monumento": "Micro teatro de Lima",
  "Descripcion": "The Barranco Microteatro de Lima is a unique cultural institution in Lima, Peru, offering short plays that last no longer than 15 minutes. The intimate theater experience and diverse range of plays make it a great destination for theaterlovers visiting the city. In addition to the plays, the Microteatro de Lima also hosts various cultural events and workshops, making it a hub for the artistic community in Barranco. Dont miss this opportunity to experience Limas vibrant cultural scene.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos%20barranco/MICROTEATRO%201.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Barranco",
  "Latitud": 12.1502063721294,
  "Longitud": 77.0218241351487,
  "Monumento": "Barranco Electricity Museum",
  "Descripcion": "The Electricity Museum of Barranco offers a fascinating look at the history of electricity and its impact on society. Housed in a historic building that once served as the citys first power station, the museum features a range of exhibits and interactive displays that trace the development of the technology from its earliest days to the modern era. With its prime location in the heart of Barranco, its the perfect starting point for exploring this vibrant and eclectic neighborhood.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos%20barranco/MUSEO%20DE%20LA%20ELECTRICIDAD%201.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Barranco",
  "Latitud": 12.1486297580491,
  "Longitud": 77.020770396521,
  "Monumento": "Sanchez Carrion Boulevard",
  "Descripcion": "The Sanchez Carrion Boulevard is a charming street in the Barranco district of Lima, Peru. Named after a key figure in Perus struggle for independence, the boulevard is known for its stunning architecture, historic charm, and lively atmosphere. ",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos%20barranco/BOULEVARD%20BARRANCO%201.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Barranco",
  "Latitud": 12.1489674171792,
  "Longitud": 77.0222881841089,
  "Monumento": "La Ermita ",
  "Descripcion": "La Ermita Church in Barranco, Lima, Peru is a beautiful and historic church that is definitely worth a visit. Built in the late 19th century, the church has a charming and unique appearance, with a distinct red and white facade and ornate details throughout.The church has a rich history and has played an important role in the religious and cultural life of Barranco. It is said that the church was built on the site where a hermit once lived, hence its name La Ermita. The church has also been the site of many important events and celebrations, including weddings, baptisms, and religious festivals.One of the most interesting things about La Ermita is its connection to the Peruvian poet, Jose Carlos Mariategui. Mariategui was a frequent visitor to the church and was inspired by its beauty and spiritual significance. He even wrote a poem about the church, which has become a beloved part of Peruvian literature.Today, La Ermita Church continues to be an important cultural and religious center in Barranco. Visitors can attend mass or simply admire the churchs beautiful architecture and historic significance. Whether youre a lover of history, culture, or simply looking for a peaceful place to reflect, La Ermita Church is a mustvisit destination in Barranco.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos%20barranco/IGLESIA%20LA%20ERMITA%201.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Opera",
  "Latitud": 48.8607628272937,
  "Longitud": 2.33802487049497,
  "Monumento": "Louvre Museum",
  "Descripcion": "The Louvre Museum in Paris is housed in the former Louvre Palace, a fortress built in the late 12th century. The museum opened its doors to the public in 1793 and is made up of three wings, including the Denon Wing, home to some of the worlds most famous works of art, such as the Mona Lisa, and the Sully Wing, which focuses on the history of the Louvre and contains many antiquities, including the Venus de Milo. The museum also features several restaurants and cafes, including Cafe Marly, which overlooks the courtyard and the Louvre Pyramid.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Louvre%20Museum.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.8636044994305,
  "Longitud": 2.32789126371465,
  "Monumento": "Jardin des Tuileries",
  "Descripcion": "The Tuileries Gardens in Paris are a beautiful and historic green space that offers a welcome respite from the city. Commissioned by Catherine de Medici in the 16th century, the gardens are famous for their bassins, sculptures, and flowers. During the French Revolution, the gardens were a gathering place for political rallies, and in the 19th century, they were the site of several important battles and military parades. Today, the gardens are a popular destination for tourists and locals alike, offering a peaceful walk among the sculptures and flowers, or a relaxing spot to sit and soak up the sun.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Jardin%20des%20Tuileries.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.8640848605527,
  "Longitud": 2.33711985054937,
  "Monumento": "Palais Royal",
  "Descripcion": "The Palais Royal is a mustvisit site in Paris. It was built for Cardinal Richelieu in the 17th century and became the residence of Louis XIV before he moved to Versailles. Today, it is famous for its unique blend of classical and modern architecture, beautiful courtyard, and historic significance. Visitors can explore art galleries, antique shops, and highend fashion boutiques or relax in the park outside with its beautiful fountains, landscaped gardens, and unique sculptures. With its rich history and cultural significance, the Palais Royal is a destination that every tourist should have on their list.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Palais%20Royal.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.8675628424539,
  "Longitud": 2.32982469764792,
  "Monumento": "Place Vendome",
  "Descripcion": "Place Vendôme is a historic square in Paris known for its luxury shops and landmarks. The Vendôme Column, standing at over 140 feet tall, celebrates Napoleons victory at the Battle of Austerlitz. The Ritz Paris is a famous hotel in the square, having hosted celebrities and historical figures. The squares prestigious jewelers, including Cartier and Van Cleef & Arpels, offer a glimpse into the world of Parisian luxury.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Place%20Vendome.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.8596460013873,
  "Longitud": 2.34178026370253,
  "Monumento": "SaintGermain lAuxerrois Church",
  "Descripcion": "The SaintGermain lAuxerrois Church is a stunning RomanesqueGothicstyle church located in the heart of Paris. It is the oldest church in Paris, named after Germanus of Auxerre, the Bishop of Auxerre. It was the site of many significant events in French history, including the infamous Saint Bartholomews Day Massacre in 1572. The churchs bell tower offers a breathtaking view of the city, and it is the final resting place of many Merovingian kings. A visit to this church is a must for anyone interested in French history.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Saint%20Germain%20Auxerrois%20Church.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.8584200174938,
  "Longitud": 2.33806629623491,
  "Monumento": "Pont Des Arts",
  "Descripcion": "The Pont des Arts is a pedestrian bridge that spans the Seine River and connects the Institut de France and the Louvre Museum. The bridge was known for the tradition of lovers attaching locks to the bridges railings as a symbol of their eternal love, but the locks caused damage to the bridges structure. In 2015, the city of Paris removed all of the locks and installed plexiglass panels in their place. Today, the bridge offers stunning views of the Seine River and the surrounding Parisian architecture and is a popular destination for tourists.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Pont%20Des%20Arts.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.8632275003965,
  "Longitud": 2.33465321102299,
  "Monumento": "Musee des Arts Decoratifs",
  "Descripcion": "The Musee des Arts Decoratifs is a fascinating museum that features over 150,000 objects from various periods and styles, including furniture, textiles, ceramics, and glassware. Highlights of the museum include the toy gallery, showcasing an extensive collection of toys and games, and the fashion and textile gallery, with over 7,000 pieces from various periods. In addition to the permanent collection, the museum hosts temporary exhibitions throughout the year, featuring works by famous artists and designers from around the world.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Musee%20des%20Arts%20Decoratifs.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.8639224727622,
  "Longitud": 2.32264021028297,
  "Monumento": "Musee de lOrangerie",
  "Descripcion": "Located in the Tuileries Gardens, the Musee de lOrangerie is a small but significant museum featuring an impressive collection of Impressionist and PostImpressionist art, including the famous Water Lilies paintings by Claude Monet. The museum also hosts temporary exhibitions showcasing modern and contemporary art.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Musee%20de%20l%20Orangerie.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.8668014953494,
  "Longitud": 2.35638243431329,
  "Monumento": "Museum of Arts and Crafts",
  "Descripcion": "The Museum of Arts and Crafts, or Musee des Arts et Metiers in French, is an incredible museum in Paris dedicated to science, technology, and industry. With over 80,000 objects on display, including the original Foucaults pendulum and rare 16thcentury clocks, this museum offers a fascinating look into the evolution of invention and technology.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Museum%20of%20Arts%20and%20Crafts.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.8580974314161,
  "Longitud": 2.34774117438599,
  "Monumento": "Châtelet Theatre",
  "Descripcion": "The Châtelet Theatre is a historic theatre located in the heart of Paris. Established in 1862, it has been the site of many notable productions, including the Paris premiere of Claude Debussys Le Martyre de saint Sebastien in 1911. Today, the theatre continues to be a beloved institution in Paris, offering a range of productions throughout the year from classic operas to contemporary dance performances.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Chatelet%20Theatre.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.8636413513841,
  "Longitud": 2.3365491404127,
  "Monumento": "French Comedy Theatre",
  "Descripcion": "The French Comedy Theatre, or La ComedieFrançaise, is the oldest national theater company in the world. Established in 1680, it is a symbol of French culture and prestige. The theater produces classical French plays, as well as contemporary works and touring productions. Visitors can take guided tours of the theater and participate in educational programs. A mustsee destination for theater lovers visiting Paris.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/French%20Comedy%20Theatre.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.8625386604549,
  "Longitud": 2.34459046475632,
  "Monumento": "Les Halles",
  "Descripcion": "Les Halles is a lively district in Paris, known for its modern shopping mall, the Forum des Halles, and historic churches like SaintEustache. Once the site of a large central market, Les Halles is a mustvisit destination for anyone looking to experience the vibrant culture and history of Paris.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Les%20Halles.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.8618570782961,
  "Longitud": 2.33296751213127,
  "Monumento": "Arc de Triomphe du Carrousel",
  "Descripcion": "The Arc de Triomphe du Carrousel is a beautiful triumphal arch located in Paris Louvre district. It was built to commemorate Napoleons victories and is adorned with sculptures and reliefs that depict his military campaigns. The arch is topped with four bronze horses that were originally located in Constantinople and taken to Venice during the Fourth Crusade. Napoleon seized the horses in 1797 and placed them atop the arch, but they were returned to Venice in 1815. The horses currently atop the arch are replicas.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Arc%20de%20Triomphe%20du%20Carrousel.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.8579265711791,
  "Longitud": 2.34226149068947,
  "Monumento": "Pont Neuf / New Bridge",
  "Descripcion": "The Pont Neuf is the oldest standing bridge in Paris, built in the late 16th century. Its 381 mascarons are a unique feature, each one carved with a different mythological figure or animal. The equestrian statue of King Henry IV in the center of the bridge is a popular attraction, and the bridge also has a dark past as the site of the execution of Jacques de Molay, the last Grand Master of the Knights Templar.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Pont%20Neuf%20%20New%20Bridge.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.8566974691195,
  "Longitud": 2.34246538144701,
  "Monumento": "Place Dauphine",
  "Descripcion": "Welcome to Place Dauphine, one of the most charming squares in Paris. This small square, located on the Île de la Cite, is surrounded by elegant residential buildings that date back to the 17th and 18th centuries. Place Dauphine is a peaceful and quiet oasis in the heart of the city, and it has a fascinating history as a gathering place for French revolutionaries and a favorite spot for artists and writers. Today, it is a popular destination for visitors to Paris and is home to several restaurants and cafes where visitors can enjoy a meal or a drink.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Place%20Dauphine.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.859488874433,
  "Longitud": 2.33391706314835,
  "Monumento": "Pont Du Carrousel",
  "Descripcion": "The Pont des SaintsPères is a picturesque bridge connecting the Left and Right Banks of the Seine River in Paris. Constructed in the 19th century, it features four statue groups representing Industry, Abundance, The City of Paris, and the River Seine. It was reconstructed and realigned in 1935 to align with the Arc de Triomphe du Carrousel and the Louvre Museum.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Pont%20Du%20Carrousel.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.8608093147854,
  "Longitud": 2.34808634096675,
  "Monumento": "Fontaine des Innocents",
  "Descripcion": "The Fountain of the Innocents is the oldest monumental fountain in Paris, built in the 16th century to commemorate King Henry IIs entry into the city. It was designed by Pierre Lescot and sculpted by Jean Goujon. Though it initially had a limited water flow, a new aqueduct was constructed under Napoleon Bonaparte. It is a beautiful example of Renaissance architecture and a popular attraction in Paris.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Fontaine%20des%20Innocents.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.8634679096638,
  "Longitud": 2.346279811023,
  "Monumento": "Church of SaintEustache ",
  "Descripcion": "Welcome to SaintEustache Church, a stunning architectural masterpiece with a rich and fascinating history dating back to the 13th century. Named after Saint Eustace, the Roman general who converted to Christianity and is now the patron saint of hunters, the church features an impressive mix of Gothic, classical, and Renaissance elements on its exterior. The interior boasts beautiful stained glass from the 17th and 19th centuries, and an impressive pipe organ with over 8,000 pipes. The church has played an important role in the religious and cultural life of Paris, and many famous Parisians have been connected to it, such as Cardinal Richelieu and Molière.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Church%20of%20SaintEustache.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Louvre",
  "Latitud": 48.8658072408573,
  "Longitud": 2.3419126864388,
  "Monumento": "Place des Victories  Victory Square",
  "Descripcion": "Welcome to Place des Victoires, a stunning and historic square located in the heart of Paris. The square is known for its beautiful architecture and rich history. It was built in the 17th century to celebrate the victories of King Louis XIV and it was designed by the famous French architect, Jules HardouinMansart. The square is surrounded by elegant buildings and features a statue of the king at its center. Today, Place des Victoires is a popular destination for tourists who want to soak up the beauty and history of Paris.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Place%20des%20Victories%20%20Victory%20Square.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Bourse",
  "Latitud": 48.8694386863815,
  "Longitud": 2.34223712876803,
  "Monumento": "Palais Brongniart",
  "Descripcion": "The Palais Brongniart, located in the II arrondissement of Paris, used to be the historical stock exchange of Paris. Designed by architect AlexandreTheodore Brongniart, it was built from 1808 to 1813. Today, the building hosts cultural events and exhibitions.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Palais%20Brongniart.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Bourse",
  "Latitud": 48.8681821744675,
  "Longitud": 2.33604366555154,
  "Monumento": "Passage Choiseul",
  "Descripcion": "Welcome to Passage Choiseul, one of Paris charming covered passages located in the 2nd arrondissement. This passage is an extension of Rue de Choiseul, offering a delightful shopping and dining experience. Its history dates back to the early 19th century when it was built between 1826 and 1827 by architects François Mazois and Antoine Tavernier. Passage Choiseul is not only a place of commerce but also holds literary significance, as it is mentioned in novels by LouisFerdinand Celine. With its shops, restaurants, bookstores, art galleries, and more, it has something to offer every visitor. Dont miss the entrance to the Theâtre des BouffesParisiens, adding a touch of culture to this vibrant passage. At 190 meters long and 3.7 meters wide, Passage Choiseul is the longest covered passage in the city. Explore this registered historic monument and indulge in the unique atmosphere of Passage Choiseul.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Passage%20Choiseul.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Bourse",
  "Latitud": 48.8719224533921,
  "Longitud": 2.34293922876818,
  "Monumento": "The Musee Grevin ",
  "Descripcion": "The Musee Grevin is a wax museum in Paris located in the 9th arrondissement. It features over 450 wax characters from French history and modern life, including movie stars, athletes, and international figures. New figures are regularly added, and it is a popular tourist attraction with an admission fee charged.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/The%20Mus%C3%A9e%20Gr%C3%A9vin.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Bourse",
  "Latitud": 48.8629820104175,
  "Longitud": 2.34274397719626,
  "Monumento": "Bourse du Commerce",
  "Descripcion": "The Bourse de Commerce, originally used for trading in grain and other commodities, is a circular building in Paris. It was built between 1763 and 1767 with a wooden dome, which was later replaced in 1811 by a copper one. Today, it is the Parisian exhibition site of the Pinault Collection.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Bourse%20du%20Commerce.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Bourse",
  "Latitud": 48.8684906178574,
  "Longitud": 2.33542623911873,
  "Monumento": "Theâtre des BouffesParisiens",
  "Descripcion": "The Theâtre des BouffesParisiens is a Parisian theatre founded in 1855 by Jacques Offenbach for the performance of operetta. The theatre is located in the 2nd arrondissement at 4 rue Monsigny with an entrance at the back at 65 Passage Choiseul.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Theatre%20des%20BouffesParisiens.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Bourse",
  "Latitud": 48.8706671836092,
  "Longitud": 2.34815230603224,
  "Monumento": "Le Grand Rex",
  "Descripcion": "The Grand Rex is a famous movie theater in the 2nd arrondissement of Paris, designated a Monument historique since 1981. With over a million visitors annually, it has a seating capacity of more than 2700 people. Designed by Auguste Bluysen and John Eberson, it was opened in 1932 by Jacques Haïk. The cinemas grand hall has over 400 decors of phantasmatic cities and an Art Deco atmosphere. It has undergone several renovations, including adding the Great Large, Europes largest screen, in 1988. The Grand Rex is renowned for hosting premieres, special events, and marathons, and is located near the BonneNouvelle station, served by Metro lines 8 and 9, and bus lines 20, 32, and 39.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Le%20Grand%20Rex.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Bourse",
  "Latitud": 48.8651339475758,
  "Longitud": 2.33778520820069,
  "Monumento": "The PalaisRoyal garden",
  "Descripcion": "The PalaisRoyal garden in Paris is the only garden classified as a Remarkable Garden by the French Ministry of Culture. It was created in 1633 for Richelieu and redesigned by Andre Le Nôtre in 1674. The garden covers 20,850 square meters and has 500 trees, a central basin with a water jet, and two long lawns bordered with flowerbeds. The garden is separated from the palaces inner courtyard by the Orleans Gallery, which is known for the controversial Buren Columns, a work of art comprising of 260 black and white striped octagonal columns.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/The%20PalaisRoyal%20garden.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Temple",
  "Latitud": 48.8598109469578,
  "Longitud": 2.36264453884112,
  "Monumento": "The Musee Picasso",
  "Descripcion": "The Musee Picasso is an art gallery in Paris, France dedicated to the works of Pablo Picasso. The museum collection includes over 5,000 works of art, as well as tens of thousands of archived pieces from Picassos personal collection. The building housing the collection, the Hôtel Sale, was built in the 17th century for a wealthy tax farmer and has since been restored. The museum largely follows a chronological sequence, displaying paintings, drawings, sculptures, and prints.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/The%20Mus%C3%A9e%20Picasso.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Temple",
  "Latitud": 48.8675167282824,
  "Longitud": 2.36382173519711,
  "Monumento": "Place de la Republique",
  "Descripcion": "The Place de la Republique is a square in Paris named after the French Republics. It features a 31 feet bronze statue of Marianne, surrounded by three statues symbolizing liberty, equality, and fraternity. The Metro station of Republique lies beneath the square, and it is one of the networks main transfer points on the Rive Droite.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Place%20de%20la%20R%C3%A9publique.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Temple",
  "Latitud": 48.8634138419285,
  "Longitud": 2.36788745575468,
  "Monumento": "Cirque dHiver Bouglione",
  "Descripcion": "The Cirque dHiver, located in Paris, has been a prominent venue for circuses, exhibitions, musical concerts, and other events since it was opened in 1852 by Emperor Napoleon III. The nearest metro station is Filles du Calvaire.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Cirque%20dHiver%20Bouglione.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Temple",
  "Latitud": 48.8705943455456,
  "Longitud": 2.37351832212825,
  "Monumento": "Canal SaintMartin",
  "Descripcion": "The Canal SaintMartin is a 4.6 km long canal in Paris, built in the 19th century to supply the city with fresh water and goods. The canal is a popular destination for Parisians and tourists, with cruises and restaurants available.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Canal%20SaintMartin.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Temple",
  "Latitud": 48.8629667146397,
  "Longitud": 2.36208622747336,
  "Monumento": "Marche des Enfants Rouges",
  "Descripcion": "The Marche des Enfants Rouges is the oldest covered market in Paris, established in 1628. Its located in the Marais arrondissement and offers fresh produce, flowers, bread, and cooked meals.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Marche%20des%20Enfants%20Rouges.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Temple",
  "Latitud": 48.8616886289987,
  "Longitud": 2.35561594041259,
  "Monumento": "Jardin de Anna Frank",
  "Descripcion": "This community garden surrounded by a high wall tracing city walls of Paris boasts 2,200 m² of land. Its name pays homage to Anne Frank (19291945), a victim of Nazi barbarism during World War II. It is composed of a central plot dating from the 17th century, a contemporary shady space (in which a graft of the chestnut tree that Anne Frank admired from her window was planted on 20 June 2007) and an orchard.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Jardin%20de%20Anna%20Frank.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Temple",
  "Latitud": 48.8615021210263,
  "Longitud": 2.35901041582824,
  "Monumento": "Musee de la Chasse",
  "Descripcion": "The Musee de la Chasse et de la Nature is a private museum in Paris that focuses on the relationship between humans and the natural environment through the traditions and practices of hunting. The museum was founded in 1964 by François Sommer, an industrialist rugmaker, and his wife Jacqueline. It is described as one of the most rewarding and inventive museums in Paris.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Mus%C3%A9e%20de%20la%20Chasse.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Hotel de Ville",
  "Latitud": 48.8530670043076,
  "Longitud": 2.35025614836015,
  "Monumento": "Notre Dame Cathedral",
  "Descripcion": "NotreDame is a famous Catholic cathedral located in the heart of Paris. Built between 1163 and 1260, the cathedral is renowned for its Gothic architecture, with unique features such as rib vaults, flying buttresses, and enormous rose windows. It is a national symbol and has played a significant role in French history, being the site of Napoleon Is coronation and the funerals of many French presidents. The cathedral inspired Victor Hugos novel, NotreDame de Paris, and underwent a major restoration in the 19th century. In 2019, a devastating fire caused significant damage to the cathedral, but reconstruction efforts are underway.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Notre%20Dame%20Cathedral.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Hotel de Ville",
  "Latitud": 48.8607901979991,
  "Longitud": 2.35358610122629,
  "Monumento": "Centre Pompidou",
  "Descripcion": "The Centre Pompidou is a multiuse cultural center located in the 4th arrondissement of Paris. It was designed by Richard Rogers, Su Rogers, Renzo Piano, and Gianfranco Franchini in the style of hightech architecture. The building houses the Bibliothèque publique dinformation, the largest museum for modern art in Europe called the Musee National dArt Moderne, and a center for music and acoustic research called IRCAM. It was named after Georges Pompidou, the President of France from 1969 to 1974 who commissioned the building, and was officially opened on 31 January 1977 by President Valery Giscard dEstaing.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Centre%20Pompidou.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Hotel de Ville",
  "Latitud": 48.855725730867,
  "Longitud": 2.36603198884086,
  "Monumento": "Place des Vosges",
  "Descripcion": "Place des Vosges is the oldest planned square in Paris, located in the Marais district. Originally known as Place Royale, it was built from 1605 to 1612 by Henri IV and served as a fashionable and expensive square to live in during the 17th and 18th centuries. Today, the square is planted with a bosquet of mature lindens surrounded by clipped lindens.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Place%20des%20Vosges.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Hotel de Ville",
  "Latitud": 48.8611372218532,
  "Longitud": 2.35561119678927,
  "Monumento": "Museum of Judaic Arts and History",
  "Descripcion": "The Musee dArt et dHistoire du Judaïsme (mahJ) is the largest museum of Jewish art and history in France, located in Paris Marais district. The museum houses a vast collection of religious objects, archives, manuscripts, and works of art that tell the story of Jews in Europe and North Africa from the Middle Ages to the 20th century. The mahJ also features a bookshop, media library, auditorium, and educational workshops.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Museum%20of%20Judaic%20Arts%20and%20History.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Hotel de Ville",
  "Latitud": 48.8571939318623,
  "Longitud": 2.36287935446004,
  "Monumento": "Musee Carnavalet",
  "Descripcion": "The Musee Carnavalet in Paris is a museum dedicated to the history of the city. It occupies two neighboring mansions  the Hôtel Carnavalet and the former Hôtel Le Peletier de Saint Fargeau. The museum contains furnished rooms from different periods of Parisian history, historic objects, and a large collection of paintings depicting Parisian life.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Mus%C3%A9e%20Carnavalet.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Hotel de Ville",
  "Latitud": 48.8565955153596,
  "Longitud": 2.35271390418287,
  "Monumento": "Hotel de Ville",
  "Descripcion": "The Hôtel de Ville is the city hall of Paris, located on the Place de lHôteldeVille. It has been the headquarters of the municipality of Paris since 1357 and serves multiple functions, housing the local government council, the Mayors of Paris and their cabinets, and also serves as a venue for large receptions.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Hotel%20de%20Ville.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Hotel de Ville",
  "Latitud": 48.8582026167554,
  "Longitud": 2.34896084417748,
  "Monumento": "Tour SaintJacques",
  "Descripcion": "The Tour SaintJacques is a Gothic tower in Paris, France, which was built in 1509 to 1523. It is the only surviving part of the former Church of SaintJacquesdelaBoucherie, which was demolished in 1797 during the French Revolution. The tower was built in honor of Saint James the Greater and is now considered a national historic landmark.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Tour%20SaintJacques.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Hotel de Ville",
  "Latitud": 48.8569022915714,
  "Longitud": 2.35186173061573,
  "Monumento": "Place de lHôtel de Ville ",
  "Descripcion": "The Place de lHôtel de Ville in Paris was once known as the Place de Grève, a sandy location on the riverbank where the first riverine harbor of Paris was established. It was also used for public meetings and public executions in early Paris.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Place%20de%20lH%C3%B4tel%20de%20Ville.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Hotel de Ville",
  "Latitud": 48.8673238765554,
  "Longitud": 2.28694733158843,
  "Monumento": "Musee national de la Marine",
  "Descripcion": "The Musee national de la Marine, located in the Palais de Chaillot in Paris, is a maritime museum with annexes in other French cities. Its permanent collection dates back to Louis XV, and it was opened to the public in 1943.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Mus%C3%A9e%20national%20de%20la%20Marine.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Pantheon",
  "Latitud": 48.8465226985135,
  "Longitud": 2.34625760418226,
  "Monumento": "The Pantheon",
  "Descripcion": "The Pantheon in Paris is a monument dedicated to the great men of France. It was originally built as a church in the 18th century and has since been used for a variety of purposes, including as a mausoleum and a secular temple. The dome of the Pantheon is one of the tallest in the world, and its interior features impressive paintings and sculptures. The Pantheon is also known for its famous Foucault pendulum, which demonstrates the rotation of the Earth.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/The%20Pantheon.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Pantheon",
  "Latitud": 48.8463346385074,
  "Longitud": 2.33755746370172,
  "Monumento": "Luxembourg Garden",
  "Descripcion": "The Jardin du Luxembourg, also known as the Luxembourg Garden, is a beautiful park located in the 6th arrondissement of Paris, France. It covers 23 hectares and is known for its lawns, treelined promenades, tennis courts, flowerbeds, model sailboats, and picturesque Medici Fountain. The garden was created in 1612 when Marie de Medici constructed the Luxembourg Palace as her new residence. Today, the garden is owned by the French Senate and is open to the public. Tourists can enjoy the calm atmosphere, visit the orchard of apple and pear trees, watch the model boats in the Grand Bassin, and explore the various statues and sculptures.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Luxembourg%20Garden.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Pantheon",
  "Latitud": 48.8506315280801,
  "Longitud": 2.34469234041192,
  "Monumento": "The Musee de Cluny",
  "Descripcion": "The Musee de Cluny, officially known as the Musee de ClunyMusee National du Moyen Âge, is a medieval art museum located in the 5th arrondissement of Paris. The building combines the Romanera Thermae and the 15thcentury Hôtel de Cluny, which was the Parisian mansion of the Abbey. The museum is famous for its collection of art from the Middle Ages, including the series of six 15thcentury tapestries known as The Lady and the Unicorn.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/The%20Mus%C3%A9e%20de%20Cluny.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Pantheon",
  "Latitud": 48.8444172894141,
  "Longitud": 2.34504650233365,
  "Monumento": "Musee Curie",
  "Descripcion": "The Musee Curie in Paris is a historical museum dedicated to radiological research, located at 1, rue Pierre et Marie Curie. The museum was established in 1934 on the ground floor of the Curie Pavilion of the Institut du Radium, and features a permanent exhibition on radioactivity and its applications, especially in medicine, as well as archives and documentation on the Curies, JoliotCuries, and the history of radioactivity and oncology.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Mus%C3%A9e%20Curie.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Pantheon",
  "Latitud": 48.8534468413726,
  "Longitud": 2.34446872691858,
  "Monumento": "Fontaine SaintMichel",
  "Descripcion": "The Fontaine SaintMichel is a monumental fountain located in Place SaintMichel in the 6th arrondissement in Paris. It was constructed in 1858–1860 during the French Second Empire by the architect Gabriel Davioud.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Fontaine%20SaintMichel.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Pantheon",
  "Latitud": 48.8472800793239,
  "Longitud": 2.35792815020828,
  "Monumento": "Sorbonne University",
  "Descripcion": "Sorbonne University is a prestigious public research university located in Paris, France, with a history dating back to 1257. Its reputation is reflected in the number of Nobel Prizes, Fields Medals, and Turing Awards won by its alumni and professors. The university is highly regarded for its academic and industry programs, with top rankings in natural sciences, mathematics, classics, and ancient history.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Sorbonne%20University.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Luxembourg",
  "Latitud": 48.8465391713305,
  "Longitud": 2.34861540972769,
  "Monumento": "eglise SaintetienneduMont",
  "Descripcion": "SaintetienneduMont is a historic church in Paris, France, located in the 5th arrondissement near the Pantheon. It is the final resting place of Blaise Pascal and Jean Racine and contains the shrine of St. Geneviève, the patron saint of Paris. The church has an impressive sculpted tympanum, The Stoning of Saint Stephen, by French sculptor GabrielJules Thomas. The renowned organist Maurice Durufle was the Titular Organist at the church from 1929 until his death in 1986. The churchs history dates back to the GalloRoman era and has undergone several changes in style and restoration over the years.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/%C3%89glise%20Saint%C3%89tienneduMont.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Pantheon",
  "Latitud": 48.8445199997591,
  "Longitud": 2.35038305945048,
  "Monumento": "Place de la Contrescarpe",
  "Descripcion": "Place de la Contrescarpe is a square in the 5th arrondissement of Paris, located along Rue Mouffetard. It has a circular traffic island in the middle, partly occupied by a public fountain, and contains many cafes popular with tourists.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/%C3%89glise%20Saint%C3%89tienneduMont.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Pantheon",
  "Latitud": 48.8423260306188,
  "Longitud": 2.35014497719498,
  "Monumento": "Rue Mouffetard",
  "Descripcion": "Rue Mouffetard is one of the oldest and most vibrant neighborhoods in Paris, located in the fifth arrondissement. The street has a rich history dating back to Neolithic times and was originally a Roman road. Today, it is a predominantly pedestrian avenue with numerous shops, restaurants, and cafes, as well as a regular openair market. Its name has evolved over the centuries, appearing as rue Montfetard, Maufetard, Mofetard, Moufetard, Mouflard, Moufetard, Moftard, Mostard, and also as rue SaintMarcel, rue du Faubourg SaintMarceau, and rue de la Vieille Ville SaintMarcel.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Rue%20Mouffetard.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Pantheon",
  "Latitud": 48.8432152282371,
  "Longitud": 2.33398326795269,
  "Monumento": "Musee Zadkine",
  "Descripcion": "The Musee Zadkine is a museum located in the 6th arrondissement of Paris that showcases the work of Russian sculptor Ossip Zadkine. The museum contains around 300 sculptures, as well as drawings, photographs, and tapestries, and has added to its collection through purchases. Since 1995, the museum has hosted 34 contemporary art exhibits each year.The museum is housed in the former home and studio of Zadkine and was established by his wife, Valentine Prax. It was inaugurated in 1982, following her death, and has a beautiful garden that visitors can enter free of charge. The museum underwent renovations in 2012 and has since reopened its doors with a new museography designed to better reflect the spirit of the workshop.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Mus%C3%A9e%20Zadkine.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Luxembourg",
  "Latitud": 48.8509532878943,
  "Longitud": 2.33371953486652,
  "Monumento": "Fontaine SaintSulpice",
  "Descripcion": "The Fontaine SaintSulpice is a fountain located in the 6th arrondissement of Paris. It was built between 1843 and 1848 by architect Louis Visconti and features four French religious figures known for their eloquence. The fountain was commissioned by the prefect of the Seine, who wanted to decorate the city with impressive water features. The fountain was criticized upon opening for its incoherent iconography and details.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Fontaine%20SaintSulpice.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Luxembourg",
  "Latitud": 48.849075833486,
  "Longitud": 2.33496193061524,
  "Monumento": "Musee du Luxembourg",
  "Descripcion": "The Musee du Luxembourg is a museum located in the 6th arrondissement of Paris, France. Established in 1750, it was initially an art museum located in the east wing of the Luxembourg Palace, displaying the Kings collection which included Titians The Madonna of the Rabbit, Da Vincis Holy Family, and nearly a hundred other Old Master works. Nowadays, it hosts temporary exhibitions and is part of the Reunion des Musees Nationaux. The building that now houses the museum was once an orangery of the Palace, and it was here that the museum moved in 1884. Dont miss the chance to visit this historical landmark and admire some of the greatest works of art in Paris.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Mus%C3%A9e%20du%20Luxembourg.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Luxembourg",
  "Latitud": 48.8573991135466,
  "Longitud": 2.3375674790444,
  "Monumento": "Institut de France ",
  "Descripcion": "The Institut de France is a learned society consisting of five academies, including the prestigious Academie Française. Located in the 6th arrondissement of Paris, the institute manages over 1,000 foundations, museums, and chateaux that are open for visit. It awards prizes and subsidies amounting to over €27 million per year, mostly on the recommendation of its academies. The building was originally the Collège des QuatreNations, a school established by Cardinal Mazarin in 1661 for students from new provinces attached to France under Louis XIV.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Institut%20de%20France.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Luxembourg",
  "Latitud": 48.8496079311233,
  "Longitud": 2.33869226794431,
  "Monumento": "OdeonTheâtre de lEurope",
  "Descripcion": "The OdeonTheâtre de lEurope is one of Frances six national theatres, located at 2 rue Corneille in the 6th arrondissement of Paris. The original building was constructed for the Theâtre Français between 1779 and 1782, and was inaugurated by MarieAntoinette in 1782. Beaumarchais play The Marriage of Figaro premiered two years later. The present structure, designed by Pierre Thomas Baraguay, was opened in September 1819. In 1990, the theater was given the sobriquet Theâtre de lEurope.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Od%C3%A9onTh%C3%A9%C3%A2tre%20de%20lEurope.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Luxembourg",
  "Latitud": 48.8513759063767,
  "Longitud": 2.33370782324081,
  "Monumento": "Place SaintSulpice",
  "Descripcion": "Welcome to Place Saint Sulpice, a charming public square in the heart of Paris. Dominated by the magnificent Church of SaintSulpice, this square was designed as a peaceful garden back in 1754. At the center of the square, youll find the Fontaine SaintSulpice, also known as the Fountain of the Four Bishops. Take a moment to admire the statues of the four esteemed bishops, each representing a different direction. Explore the square, and dont forget to notice the beautiful chestnut trees and the City Hall of the 6th arrondissement. If youre feeling thirsty, Cafe de la Mairie is a popular spot known for its association with writers and students. ",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Place%20SaintSulpice.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Palais Borboun",
  "Latitud": 48.8513759063767,
  "Longitud": 2.33370782324081,
  "Monumento": "Eiffel Tower",
  "Descripcion": "Welcome to the iconic Tour Eiffel! This magnificent structure is a symbol of Paris and a mustvisit attraction. The Eiffel Tower stands at a height of 330 meters (1,083 feet) and is divided into three levels, each offering a unique experience.Level 1: This level, located at 57 meters (187 feet) above the ground, is perfect for those seeking a panoramic view of Paris. You can admire the citys landmarks like the Arc de Triomphe, ChampsElysees, and the Seine River. There are also souvenir shops where you can find Eiffel Towerthemed merchandise to take home. Additionally, Level 1 features a glass floor, which provides a thrilling perspective as you look down on the bustling activity below.Level 2: Situated at 115 meters (377 feet), Level 2 provides an even more breathtaking view. From this level, you can see famous landmarks in detail and appreciate the architectural splendor of Paris. This level offers two restaurants: Le Jules Verne, a gourmet dining experience located 125 meters (410 feet) above the ground, and the 58 Tour Eiffel, a more casual option with stunning views. Make sure to reserve a table in advance to secure your spot!Level 3: The highest accessible level, standing at 276 meters (905 feet), offers an unparalleled panorama. From here, youll be able to witness the stunning skyline of Paris, spot Montmartre, NotreDame, and other landmarks in the distance. Although there are no restaurants on this level, youll find a champagne bar where you can savor a glass of champagne while taking in the mesmerizing views.Remember, the Eiffel Tower can get crowded, so its advisable to book tickets in advance. Enjoy the mesmerizing views and capture unforgettable memories of Paris from the heights of this architectural marvel!",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Eiffel%20Tower.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Palais Borboun",
  "Latitud": 48.8620515022191,
  "Longitud": 2.31906682270009,
  "Monumento": "Palais Bourbon",
  "Descripcion": "The Palais Bourbon, also known as the Palais Bourbon in French, is a government palace located in the seventh district of Paris, on the left bank of the Seine, facing the Place de la Concorde across the river. It serves as the seat of the National Assembly, the lower house of the French parliament.Originally built in 1722 as a country house surrounded by gardens for LouiseFrançoise de Bourbon, Duchess of Bourbon, a legitimized daughter of Louis XIV, the palace was nationalized during the French Revolution. During the Directory period from 1795 to 1799, it served as the meeting place of the Council of Five Hundred, the legislative body that elected the five members of the Directory. In 1806, Napoleon Bonaparte added a classical colonnade to its entrance by the Seine.The Palais Bourbon complex currently includes the Hôtel de Lassay, on the west side of the Palais Bourbon, which serves as the official residence of the President of the National Assembly.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Palais%20Bourbon.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Palais Borboun",
  "Latitud": 48.8600743154662,
  "Longitud": 2.32720512824543,
  "Monumento": "DOrsay Museum ",
  "Descripcion": "Welcome to the Musee dOrsay, a magnificent museum located on the Left Bank of the Seine River in Paris. Housed in a beautifully restored former railway station, this worldrenowned institution showcases an impressive collection of art from the 19th and early 20th centuries.The Musee dOrsay is a paradise for art enthusiasts. As you step inside, youll be greeted by an extraordinary array of masterpieces by renowned artists such as Monet, Van Gogh, Renoir, and Degas. The museums vast galleries span multiple floors, offering a captivating journey through the artistic movements of Impressionism, PostImpressionism, and beyond.Be sure to explore the museums iconic clock tower, which offers breathtaking views of the surrounding cityscape. You can also relax and take in the beauty of the Seine River from the museums terrace cafe.A visit to the Musee dOrsay is an opportunity to immerse yourself in the vibrant world of 19thcentury art. Whether youre a seasoned art connoisseur or simply appreciate beauty, this museum is a mustvisit destination in Paris.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/DOrsay%20Museum.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Palais Borboun",
  "Latitud": 48.8609692134495,
  "Longitud": 2.31320729816269,
  "Monumento": "Esplanade des Invalides",
  "Descripcion": "Welcome to the Esplanade des Invalides, a picturesque public square located between Place des Invalides and Quai dOrsay in Paris. This magnificent esplanade showcases the splendid northern facade of the renowned Hôtel des Invalides. As you explore this historic site, youll notice the perfect blend of natural beauty and architectural grandeur.  Named after the Hôtel des Invalides it leads to, the Esplanade has a rich history. It was originally designed in 1704 as a vegetable garden where war veterans could cultivate crops and engage with the local community. Over the years, it has witnessed numerous significant events, including the celebration of August 10, 1793, the Industrial Exposition in 1806, and the solemn ceremony of the return of Napoleons ashes in 1840.Immerse yourself in the captivating ambiance of the Esplanade des Invalides, where history and beauty converge.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Esplanade%20des%20Invalides.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Palais Borboun",
  "Latitud": 48.8559062248707,
  "Longitud": 2.31307619578576,
  "Monumento": "Musee de lArmee",
  "Descripcion": "Welcome to the Musee de lArmee, a prestigious national military museum located in Les Invalides, Paris. Embark on a journey through the rich tapestry of French military history as you explore this captivating institution.Step into the Main Courtyard, the heart of the museum, where an impressive collection of French field artillery awaits. Discover the evolution of weaponry and the stories of courageous French artillerymen who shaped the nations defense.Continue your exploration in the Armor and Weapons section, where ancient and medieval artifacts transport you to eras of knights and warriors. Marvel at the intricate armor, swords, and shields that showcase the craftsmanship of the past.Conclude your visit with a glimpse into the Modern and Contemporary Departments, where youll encounter the political, social, and industrial transformations that influenced Frances military might. From the reign of Louis XIV to the defining moments of the two world wars, delve into the lives of soldiers, admire their uniforms, and witness the objects that accompanied them on the battlefield.Join us at the Musee de lArmee and immerse yourself in the captivating history of the French military.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Mus%C3%A9e%20de%20lArm%C3%A9e.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Palais Borboun",
  "Latitud": 48.8639841747813,
  "Longitud": 2.31419199948021,
  "Monumento": "Pont Alexandre III",
  "Descripcion": "The Pont Alexandre III is an iconic bridge that spans the Seine River in Paris, France. Connecting the Champselysees quarter with the Invalides and Eiffel Tower areas, it is renowned for its exquisite beauty and ornate design. Classified as a French monument historique since 1975, the bridge was built between 1896 and 1900 in the BeauxArts architectural style. It pays homage to Tsar Alexander III, who played a significant role in the FrancoRussian Alliance. The bridges impressive steel arch, standing at 6 meters high, is a marvel of engineering. Adorned with grand Art Nouveau lamps, cherubs, nymphs, and winged horses, it creates a visually stunning spectacle. The Pont Alexandre III is not only a functional structure but also a symbol of elegance, craftsmanship, and cultural significance in the heart of Paris.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Pont%20Alexandre%20III.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Palais Borboun",
  "Latitud": 48.8610114596864,
  "Longitud": 2.31992505477963,
  "Monumento": "The National Assembly",
  "Descripcion": "The National Assembly, the lower house of the French Parliament, holds a crucial role in the legislative process. With 577 deputes representing singlemember constituencies, it is responsible for enacting laws and shaping the political landscape of France. The deputes, elected for a fiveyear term, play a vital role in voicing the concerns and aspirations of their constituents. Led by the president of the National Assembly, they work in collaboration with the Senate to ensure a balanced and effective governance structure. The Assemblys official seat is the Palais Bourbon in Paris, a historic landmark that has witnessed countless debates and decisions shaping the nations destiny. As a cornerstone of democracy, the National Assembly serves as a platform for diverse political ideologies and a forum for vigorous discussions on policies and legislation.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/The%20National%20Assembly.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Palais Borboun",
  "Latitud": 48.8567566648762,
  "Longitud": 2.31273997269905,
  "Monumento": "The Hôtel des Invalides",
  "Descripcion": "The Hôtel des Invalides, known as Les Invalides, is a complex in Paris, France, dedicated to the military history of the country. Originally built as a retirement home and hospital for war veterans, it now houses museums, monuments, and a cathedral. The complex includes the Musee de lArmee, the Musee des PlansReliefs, and the Musee dHistoire Contemporaine. The prominent feature is the Dôme des Invalides, the tallest church building in Paris, standing at 107 meters. It serves as a shrine for significant military figures, including the tomb of Napoleon Bonaparte. The Invalides played a role in several pivotal events in French history, and today it remains a symbol of Frances military heritage.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/The%20H%C3%B4tel%20des%20Invalides.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Palais Borboun",
  "Latitud": 48.8554412954855,
  "Longitud": 2.3158246681385,
  "Monumento": "Musee Rodin",
  "Descripcion": "The Musee Rodin, located in Paris, France, is an art museum dedicated primarily to the works of renowned French sculptor Auguste Rodin. Established in 1919, the museum consists of two sites: the Hôtel Biron and its surrounding grounds in central Paris, as well as Rodins former residence, the Villa des Brillants, located just outside of Paris in Meudon. The museum houses a remarkable collection that includes 6,600 sculptures, 8,000 drawings, 8,000 old photographs, and 7,000 objets dart. With its vast array of artwork, the Musee Rodin attracts approximately 700,000 visitors each year, making it a popular destination for art enthusiasts from around the world.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Mus%C3%A9e%20Rodin.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Palais Borboun",
  "Latitud": 48.8557604172437,
  "Longitud": 2.29911319458363,
  "Monumento": "Champ de Mars",
  "Descripcion": "The Champ de Mars, also known as the Field of Mars, is a vast public greenspace in Paris, France. It is situated in the seventh arrondissement, between the iconic Eiffel Tower to the northwest and the ecole Militaire to the southeast. The name Champ de Mars is derived from the Campus Martius in Rome, honoring the Roman god of war. The park was historically used as a training and parade ground for the French military, reflecting its association with martial activities.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Champ%20de%20Mars.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Palais Borboun",
  "Latitud": 48.8621156414458,
  "Longitud": 2.31876701091287,
  "Monumento": "Palais Bourbon",
  "Descripcion": "The Quai dOrsay, gracefully lining the 7th arrondissement of Paris, offers a captivating riverside escape. This delightful quay on the left bank of the Seine, facing the magnificent Place de la Concorde, invites you to indulge in its scenic allure. As you explore further, youll discover that the quay transforms into the Quai AnatoleFrance to the east and the Quai Branly to the west, each with its own distinctive charm.Art enthusiasts will appreciate the Quai dOrsays deeprooted connection to French art history. For centuries, this riverside location has attracted artists seeking inspiration from the serene surroundings. It has been a muse for painters who sought to capture the enchanting ambiance of the Seines banks in their masterpieces. Embark on a leisurely stroll along this historic quay, and youll be transported back in time to an era of creativity and artistic expression.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Quai%20dOrsay.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "elysees",
  "Latitud": 48.8713794160757,
  "Longitud": 2.30239304429026,
  "Monumento": "Avenue des Champselysees",
  "Descripcion": "Welcome to the Avenue des Champselysees, a legendary street that stretches 1.9 kilometers through the heart of Paris. This iconic avenue, known as the most beautiful avenue in the whole world, is located in the 8th arrondissement, connecting the magnificent Place de la Concorde to the grandeur of the Place Charles de Gaulle, where the majestic Arc de Triomphe stands. As you walk along this historic avenue, youll be enchanted by its charm and elegance. The Champselysees is famous for its prestigious theaters, exquisite cafes, and luxury shops that showcase the height of fashion. It is also the thrilling finale of the Tour de France cycling race and the magnificent setting for the annual Bastille Day military parade. Immerse yourself in the allure of the Champselysees, where art, culture, and unparalleled beauty converge.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Avenue%20des%20Champs%C3%89lys%C3%A9es.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "elysees",
  "Latitud": 48.8739821983225,
  "Longitud": 2.29508114115419,
  "Monumento": "Arc de Triomphe",
  "Descripcion": "The Arc de Triomphe, located at the western end of the Champselysees in Paris, is one of the most famous monuments in France. Designed by Jean Chalgrin and completed in 1836, it stands as a symbol of Frances military history and honors those who fought and died for the country during the French Revolutionary and Napoleonic Wars. The monument features intricate sculptures and reliefs that depict important moments in French history. Beneath the arch lies the Tomb of the Unknown Soldier, a memorial dedicated to the unidentified soldiers who lost their lives in World War I. Visitors can climb to the top of the Arc de Triomphe for a panoramic view of Paris, taking in the beauty of the city from this iconic landmark.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Arc%20de%20Triomphe.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "elysees",
  "Latitud": 48.8534246414288,
  "Longitud": 2.30243171231718,
  "Monumento": "Grand Palais",
  "Descripcion": "Welcome to the Grand Palais, a historic site and museum complex located at the iconic Champselysees in Paris. Built for the Universal Exposition of 1900, the Grand Palais is a magnificent BeauxArts masterpiece that showcases the glory of French art. Its ornate stone façades, glass vaults, and innovative iron and steel framing make it a true architectural gem. As you explore its grand halls, youll be captivated by the impressive exhibitions and shows held within. The Grand Palais has played host to a wide range of events, from art exhibitions to riding competitions, and has witnessed the evolution of modernity. Step inside and immerse yourself in the rich history and artistic legacy of this grand venue.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Grand%20Palais.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "elysees",
  "Latitud": 48.8660058864806,
  "Longitud": 2.31490802430275,
  "Monumento": "Petit Palais",
  "Descripcion": "Welcome to the Petit Palais, a charming art museum located in the 8th arrondissement of Paris. Built for the 1900 Exposition Universelle, the Petit Palais now houses the City of Paris Museum of Fine Arts. It is situated across from the Grand Palais, on the elegant Avenue WinstonChurchill, with the Seine and Avenue des Champselysees at its sides. Designed by Charles Girault, the Petit Palais showcases the BeauxArts style, drawing inspiration from the late 17th and early 18th century French architecture. The exterior of the building features a grand central entrance, adorned with columns and a dome, while the pavilions display beautiful arched windows. Inside, the museum offers a captivating collection of artworks, including paintings by renowned artists such as Rembrandt, Rubens, Monet, and Rodin. Dont miss the stunning courtyard, a tranquil oasis within the bustling city. Explore the Petit Palais and immerse yourself in the beauty of art and history.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Petit%20Palais.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "elysees",
  "Latitud": 48.8655342631659,
  "Longitud": 2.32116059512453,
  "Monumento": "Place de la Concorde",
  "Descripcion": "Welcome to Place de la Concorde, one of Paris most significant public squares. With a size of 7.6 hectares, it is the largest square in the city. Located in the eighth arrondissement, at the eastern end of the Champselysees, this historic square has witnessed numerous notable events.Originally designed to showcase an equestrian statue of King Louis XV, the square was completed in 1772. The octagonal shape, stone bridges, and flowerbeds make it a sight to behold. The central attraction is the Luxor Obelisk, an ancient Egyptian monument gifted to France in 1833.In the squares surroundings, youll find architectural gems such as the Hôtel de la Marine and Hotel Crillon. The Tuileries Garden and the museums of the Jeu de Paume and Orangerie also border the square. Immerse yourself in the grandeur and history of Place de la Concorde.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Place%20de%20la%20Concorde.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "elysees",
  "Latitud": 48.8674549609527,
  "Longitud": 2.31734225464651,
  "Monumento": "Jardins des Champselysees",
  "Descripcion": "Welcome to the Jardin des Champselysees, a splendid public park in the heart of Paris. Spanning 13.7 hectares, this park is situated on both sides of the famous Avenue des Champselysees, between the iconic Place de la Concorde and the Rondpoint des Champselysees. Designed by Andre Le Notre in 1667, these gardens were an extension of the nearby Tuileries Palace gardens. Today, they house prominent landmarks such as the Grand Palais, the Petit Palais, theaters, and other magnificent buildings. In the 19th century, the park played a significant role in hosting the Paris International Exposition of 1855 and the Paris Universal Exposition of 1900. Immerse yourself in the beauty of the Englishstyle landscaping, strolling along winding paths, and enjoying the shade of chestnut trees. Discover statues, monuments, and quiet corners, like the Vallee Suisse, where you can escape the bustle of the city and find tranquility in natures embrace.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Jardins%20des%20Champs%C3%89lys%C3%A9es.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "elysees",
  "Latitud": 48.8756870412369,
  "Longitud": 2.31045418348275,
  "Monumento": "Musee JacquemartAndre",
  "Descripcion": "Welcome to the Musee JacquemartAndre, a private museum located at 158 Boulevard Haussmann in the heart of Paris. This museum was created from the private home of edouard Andre and Nelie Jacquemart to showcase their remarkable art collection.Step into history as you explore the museums five major divisions. The State Apartments offer a glimpse into the couples formal receptions, adorned with French school paintings and exquisite 18thcentury decorative art. Discover the informal Apartments, where business relations were received in elegant and refined salons. Marvel at the breathtaking Winter Garden, designed to surpass even the renowned Opera Garnier.Immerse yourself in Italian art in the Sculpture Gallery and the Florentine Gallery, featuring masterpieces by renowned artists such as Botticelli and Donatello. The Venetian Gallery transports you to 15thcentury Venice with its captivating artworks.Experience the charm of the Andres private world in their beautifully preserved Private Apartments.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Mus%C3%A9e%20JacquemartAndr%C3%A9.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "elysees",
  "Latitud": 48.8699317137925,
  "Longitud": 2.31645583930362,
  "Monumento": "Palais de lelysee",
  "Descripcion": "Welcome to the elysee Palace, the official residence of the President of the French Republic. Completed in 1722, this historic palace was originally built for Louis Henri de La Tour dAuvergne, a nobleman and army officer. Located on Rue du Faubourg SaintHonore near the Champselysees, the elysee Palace derives its name from the Elysian Fields of Greek mythology. Throughout its rich history, it has been home to prominent figures such as Madame de Pompadour and Joachim Murat. In 1848, the French Parliament declared it the official residence of the President. Today, the palace serves as the Presidents office, residence, and the meeting place for the Council of Ministers. While the elysee Palace remains an important symbol of French governance, its grandeur and historical significance make it a mustsee attraction in Paris.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Palais%20de%20l%C3%89lys%C3%A9e.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "elysees",
  "Latitud": 48.870857757371,
  "Longitud": 2.33175156813941,
  "Monumento": "Cafe de la Paix",
  "Descripcion": "Welcome to Cafe de la Paix, an iconic cafe situated at the corner of Boulevard des Capucines and Place de lOpera in Paris 9th arrondissement. Designed in the opulent Napoleon III style by architect Alfred Armand, this historic cafe is housed within the GrandHôtel. Since its opening on June 30, 1862, Cafe de la Paix has gained international recognition for its lavish interior, prestigious location, and esteemed clientele. Over the years, it has been frequented by notable figures such as Jules Massenet, emile Zola, Pyotr Ilyich Tchaikovsky, and Guy de Maupassant. The cafes allure extends beyond its historical significance, as it has been featured in films, music, literature, and art, captivating the imagination of artists and visitors alike. Immerse yourself in the ambiance of this cultural treasure and experience the timeless charm of Cafe de la Paix.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Caf%C3%A9%20de%20la%20Paix.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "elysees",
  "Latitud": 48.8708319143483,
  "Longitud": 2.30320072581093,
  "Monumento": "Laduree Champselysees",
  "Descripcion": "Welcome to Pâtisserie E. Laduree, the legendary French establishment renowned for its exquisite pastries and delightful candies. Established in 1862 by Louis Ernest Laduree, this iconic bakery quickly gained fame for its doubledecker macarons, with 15,000 of these delectable treats sold every day. Located in Paris, Laduree is a household name, captivating the hearts of locals and visitors alike. The bakerys charming history began on the rue Royale, where it was founded and later rebuilt after a fire during the Paris Commune uprising. The interior, adorned with chubby cherubs painted by Jules Cheret, creates an enchanting atmosphere. Experience the timeless elegance and irresistible flavors that have made Laduree an enduring symbol of French culinary artistry.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Ladur%C3%A9e%20Champs%C3%89lys%C3%A9es.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "elysees",
  "Latitud": 48.8656873965901,
  "Longitud": 2.30320654000749,
  "Monumento": "Theâtre des Champselysees",
  "Descripcion": "Discover the Theâtre des Champselysees, an exceptional entertainment venue situated at 15 Avenue Montaigne in Paris. Located near the famous Avenue des Champselysees, the theater takes its name from this prestigious neighborhood. With its iconic main hall, which can accommodate up to 1,905 spectators, and two smaller theaters, the Comedie des Champselysees and the Studio des Champselysees, this theater offers a diverse range of performances throughout the year. Immerse yourself in the beauty of this architectural masterpiece, a pioneer of Art Deco design in Paris. Dont miss the opportunity to witness the rich cultural heritage that unfolds on the stage of the Theâtre des Champselysees.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Th%C3%A9%C3%A2tre%20des%20Champs%C3%89lys%C3%A9es.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "elysees",
  "Latitud": 48.879676415597,
  "Longitud": 2.30897645464723,
  "Monumento": "Parc Monceau",
  "Descripcion": "Welcome to Parc Monceau, a charming public park nestled in the heart of Paris 8th arrondissement. Spanning 8.2 hectares, this picturesque park offers a tranquil retreat from the bustling city streets. As you enter through the main gate, youll be greeted by a magnificent rotunda, setting the stage for a delightful exploration.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Parc%20Monceau.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "elysees",
  "Latitud": 48.87963018459,
  "Longitud": 2.31244859697569,
  "Monumento": "Musee Cernuschi",
  "Descripcion": "Welcome to the Musee Cernuschi, the Asian art museum located in the heart of Paris. Founded in 1898 by Henri Cernuschi, this museum holds a remarkable collection that showcases the rich artistic heritage of Asia. As you explore the museums exhibitions, youll discover a diverse range of objects from China, Japan, Korea, and Vietnam. From exquisite bronze pieces to ancient ceramics, each artifact tells a story of craftsmanship and cultural significance. Dont miss the iconic Buddha of Meguro, a stunning Japanese bronze sculpture from the 18th century. With over 15,000 objects in its collection, the Musee Cernuschi offers a captivating journey through the art and history of Asia.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Mus%C3%A9e%20Cernuschi.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "elysees",
  "Latitud": 48.8788183726869,
  "Longitud": 2.31278726204856,
  "Monumento": "Musee Nissim de Camondo",
  "Descripcion": "Discover the Musee Nissim de Camondo, a magnificent house museum showcasing the splendor of French decorative arts from the 18th century. Located in the elegant Hôtel Camondo on the edge of Parc Monceau, this museum offers a spectacular collection of period furniture, tapestries, paintings, and porcelain. Marvel at the exquisite Aubusson tapestries, admire the masterpieces by renowned artist elisabeth VigeeLebrun, and imagine the grandeur of MarieAntoinette as you view items that once belonged to her. The museum also features exquisite Sèvres porcelain and remarkable furniture by acclaimed cabinetmakers Riesener and Oeben. Immerse yourself in the ambiance of a bygone era as you explore the elegant formal rooms, private apartments, and enchanting gardens. Step into history and experience the timeless beauty of French art and craftsmanship at the Musee Nissim de Camondo.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Mus%C3%A9e%20Nissim%20de%20Camondo.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "elysees",
  "Latitud": 48.8723464848807,
  "Longitud": 2.30079016813952,
  "Monumento": "Lido de Paris",
  "Descripcion": "Welcome to the Lido de Paris, a legendary musical theater venue located on the prestigious Champselysees. Established in 1946, the Lido is renowned for its captivating cabaret and burlesque shows that have enchanted audiences for decades. Over the years, it has hosted performances by a multitude of renowned artists, including Edith Piaf, Marlene Dietrich, Elton John, and many more. The Lido offers a unique experience of music, dance, and spectacle, where dazzling costumes, elaborate set designs, and mesmerizing choreography come together to create an unforgettable evening. Immerse yourself in the glamour and magic of the Lido as you witness the captivating performances of the talented Bluebell Girls and other exceptional artists. Get ready to be transported to a world of entertainment and extravagance that has made the Lido de Paris an iconic symbol of Parisian nightlife.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Lido%20de%20Paris.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Opera",
  "Latitud": 48.8719978986282,
  "Longitud": 2.3317301430044,
  "Monumento": "Palais Garnier",
  "Descripcion": "The Palais Garnier, also known as Opera Garnier, is a magnificent opera house located in the 9th arrondissement of Paris. Built between 1861 and 1875, it was commissioned by Emperor Napoleon III and designed by architect Charles Garnier. With its opulent interiors and extraordinary opulence, the Palais Garnier is considered one of the most famous opera houses in the world. It has become a symbol of Paris, alongside landmarks such as Notre Dame Cathedral and the Louvre. The building now serves as the primary venue for ballet performances by the Paris Opera Ballet. Visitors can explore its grand staircase, admire the richly decorated interior, and attend ballet performances in this iconic cultural institution.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Palais%20Garnier.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Opera",
  "Latitud": 48.8736294279261,
  "Longitud": 2.33213135464686,
  "Monumento": "Galeries Lafayette",
  "Descripcion": "Welcome to Galeries Lafayette, the largest department store chain in Europe. Located on Boulevard Haussmann in the 9th arrondissement of Paris, our flagship store is a true fashion destination. With over five billion euros in earnings, Galeries Lafayette is a symbol of style and luxury. Explore our 70,000 square meters of retail space, featuring a wide range of brands to suit all budgets, from readytowear to haute couture. Our art nouveau architecture, highlighted by a magnificent dome and a panoramic view of Paris, has made us a popular tourist attraction. Dont miss our weekly fashion show, a mustsee for visitors. Experience the essence of French fashion and indulge in a world of shopping delight at Galeries Lafayette.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Galeries%20Lafayette.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Opera",
  "Latitud": 48.8712448631783,
  "Longitud": 2.3378334218401,
  "Monumento": "OperaComique",
  "Descripcion": "Welcome to the OperaComique, a renowned Parisian opera company with a rich history dating back to the early 18th century. Originally founded by the popular theatres of the Parisian fairs, the OperaComique has evolved over time and continues to make significant contributions to French opera. Located in the 2nd arrondissement of Paris, close to the Palais Garnier, the companys theatre, known as the Salle Favart, offers a capacity of approximately 1,248 seats. Today, the OperaComique is officially known as the Theâtre national de lOperaComique and is committed to reconnecting with its heritage while exploring a unique repertoire to engage a wider audience. Prepare to be captivated by the timeless performances and artistic excellence that the OperaComique has to offer.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Op%C3%A9raComique.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Opera",
  "Latitud": 48.8714929713339,
  "Longitud": 2.33027672581099,
  "Monumento": "Musee du Parfum Fragonard",
  "Descripcion": "Welcome to the Musee du Parfum Fragonard, a captivating journey into the world of fragrance. Located at 9 rue Scribe in Paris, this private museum invites you to explore the history and art of perfume. Established in 1983 by Fragonard Parfumeur, the museum is housed in a magnificent Napoleon III townhouse from 1860. Step inside and discover beautifully curated exhibits showcasing antique perfume bottles, containers, toiletry sets, and stills used for steam distillation. Experience the process of perfume creation and learn about the rich heritage of perfume manufacturing and packaging. Marvel at the perfume organ, a unique display featuring ingredient bottles arranged around a balance used for fragrance mixing. Immerse yourself in the enchanting world of scents, where art, science, and craftsmanship converge. The Musee du Parfum Fragonard promises an olfactory experience like no other.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Mus%C3%A9e%20du%20Parfum%20Fragonard.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Opera",
  "Latitud": 48.8715602695369,
  "Longitud": 2.34192009025318,
  "Monumento": "Passage des Panoramas",
  "Descripcion": "Welcome to the Passage des Panoramas, the oldest covered passage in Paris. Located in the vibrant 2nd arrondissement, it stretches between Montmartre Boulevard and SaintMarc Street. This historic passage is a pioneer in covered commercial walkways, with its glazed roofing and innovative gas lights for illumination introduced in 1817. Step into a world of charm and history as you explore its elegant corridors.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Passage%20des%20Panoramas.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Opera",
  "Latitud": 48.870121099343,
  "Longitud": 2.32455019697515,
  "Monumento": "Church of SainteMarieMadeleine",
  "Descripcion": "The Church of SainteMarieMadeleine, also known as La Madeleine, is a Catholic parish church located in the 8th arrondissement of Paris. Originally planned by Louis XV as a centerpiece for the Rue Royal leading to the Place de la Concorde, the churchs construction began in 1763 but was interrupted by the French Revolution. Later, Napoleon Bonaparte transformed it into a monument celebrating his armies. Work on the church resumed after Napoleons downfall and was finally completed in 1842. With its Corinthian columns surrounding the building, the churchs exterior is a splendid example of neoclassical architecture. Inside, visitors are captivated by the intricate frescoes on the domed ceiling and magnificent sculptures by renowned French artists. The churchs rich history and remarkable artwork make it a mustvisit destination in Paris.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Church%20of%20SainteMarieMadeleine.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Opera",
  "Latitud": 48.8729795280177,
  "Longitud": 2.33317839697531,
  "Monumento": "Boulevard Haussmann",
  "Descripcion": "Boulevard Haussmann, a magnificent treelined boulevard stretching 2.53 kilometers, was created in Paris during the reign of Napoleon III under the guidance of Baron Haussmann, the Prefect of the Seine. This picturesque boulevard is flanked by elegant apartment blocks, with regulated cornice heights that create a harmonious visual appeal. Two iconic department stores, Galeries Lafayette and Au Printemps, can be found along this bustling street. Boulevard Haussmann cuts across various districts, including Madeleine, Quartier de lEurope, FaubourgduRoule, FaubourgMontmartre, and ChausseedAntin in the 8th and 9th arrondissements. Its eastern end connects with the intersection of Boulevard des Italiens and Boulevard Montmartre, where the RichelieuDrouot metro station is located. To the west, it extends up to Avenue de Friedland. The boulevard owes its name to Baron Georges Eugène Haussmann, the visionary administrator and politician who spearheaded the transformative renovations of Paris during the Second Empire.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Boulevard%20Haussmann.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Opera",
  "Latitud": 48.8718347008047,
  "Longitud": 2.3419214681395,
  "Monumento": "Passage Jouffroy",
  "Descripcion": "The Passage Jouffroy, located in the 9th arrondissement of Paris, is a charming covered passage that connects Boulevard Montmartre in the south to Rue de la GrangeBatelière in the north. Stretching about 140 meters long and 4 meters wide, it features an elegant canopy of metal and glass, with a stucco clock overlooking the alley. The passage takes a right angle turn about 80 meters from the entrance, descending stairs before continuing in a northerly direction. It is known for its unique geometric patterned floor and is home to the exit of the famous Musee Grevin. Built in 1845, the Passage Jouffroy was the first Parisian passage constructed entirely of metal and glass. It has undergone renovations and restoration to preserve its original charm. Metro stations Grands Boulevards and RichelieuDrouot provide convenient access to the passage.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Passage%20Jouffroy.jpg"
 },
 {
  "Pais": "France",
  "Ciudad": "Paris",
  "Distrito": "Opera",
  "Latitud": 48.8743812972838,
  "Longitud": 2.3449014969754,
  "Monumento": "Folies Bergère",
  "Descripcion": "Welcome to the worldrenowned Folies Bergère, a captivating cabaret music hall located at 32 Rue Richer in the 9th Arrondissement of Paris. Originally built as an opera house by architect Plumeret, it opened its doors on 2 May 1869, known as the Folies Trevise at the time. The venue was later renamed the Folies Bergère on 13 September 1872, taking inspiration from the nearby Rue Bergère.Throughout its illustrious history, the Folies Bergère has been synonymous with extravagant entertainment, featuring operettas, comic opera, popular songs, and gymnastics. The revues staged at the Folies Bergère were particularly renowned for their lavish costumes, sets, and effects, often showcasing performances by talented and daring women. Notably, in 1926, Josephine Baker captivated audiences with her sensational dance wearing a skirt made of artificial bananas.Today, the Folies Bergère continues to be an iconic symbol of French and Parisian life, preserving its legacy as a vibrant and captivating venue for unforgettable performances and shows.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_francia/Folies%20Berg%C3%A8re.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.6878435466157,
  "Longitud": 44.8095942131113,
  "Monumento": "Narikala Fortress",
  "Descripcion": "Welcome to Narikala Fortress, an ancient stronghold perched on a steep hill, overlooking the beautiful city of Tbilisi and the Mtkvari River. Established as early as the 4th century AD under King VarazBakur, it has stood the test of time, withstanding Persian invasions and Mongol rule. The fortress comprises two walled sections between Tbilisis sulfur baths and botanical gardens. At its heart, youll find the St Nicholas church, rebuilt in 1997, replicating the original 13thcentury church that was lost in a fire. This church is decorated with frescos depicting scenes from the Bible and Georgias history, making it a vibrant canvas of religious and cultural narrative. Despite the damages caused by the 1827 earthquake, Narikala remains a symbol of Tbilisis historical resilience.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Narikala%20Fortress.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.6976195565879,
  "Longitud": 44.8165325662699,
  "Monumento": "Holy Trinity Cathedral of Tbilisi",
  "Descripcion": "Welcome to the magnificent Holy Trinity Cathedral of Tbilisi, known as Sameba, a majestic symbol of Georgian spiritual and national revival. Constructed from 1995 to 2004, its one of the largest religious buildings in the world by area and the thirdtallest Eastern Orthodox cathedral. Celebrating 1,500 years of Georgian Orthodox Churchs autocephaly and 2,000 years from Jesuss birth, Sameba marries traditional Georgian architectural styles with Byzantine undertones. Within, youll find stunning murals painted by a team led by Amiran Goglidze, adorning the nine chapels, five of which are underground. Constructed mostly by anonymous donations, this sacred space represents Georgias unity and resilience.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Holy%20Trinity%20Cathedral%20of%20Tbilisi.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.693372099606,
  "Longitud": 44.8015205842732,
  "Monumento": "Freedom Square",
  "Descripcion": "Welcome to Freedom Square, the pulsating heart of Tbilisi, Georgia! This square, situated at the eastern end of Rustaveli Avenue, is steeped in history, changing names with each shift in power, from Erivansky Square to Beria Square, Lenin Square, and finally, Freedom Square. Originally named after Ivan Paskevich, a general who conquered Erivan for the Russian Empire, the square saw its identity shift numerous times during the Soviet era. Today, it stands as a symbol of Georgias sovereignty and resilience. Youll notice the Liberty Monument, a captivating statue of St George slaying the dragon, symbolizing the nations victory over oppression. Nearby, a bust of Alexander Pushkin and the Tbilisi City Assembly embellish the area. The square has been the site of many important events, like the 1907 Tiflis bank robbery and the famous speech of U.S. President George W. Bush.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Freedom%20Square.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.6997929406183,
  "Longitud": 44.7968260640022,
  "Monumento": "Rustaveli Avenue",
  "Descripcion": "Welcome to Rustaveli Avenue, Tbilisis vibrant heart named after the renowned medieval Georgian poet, Shota Rustaveli! This central avenue, formerly known as Golovin Street, is a 1.5 km stretch starting at Freedom Square, filled with rich architecture, art, and history. Along this street, youll discover key landmarks including the Parliament of Georgia, Georgian National Opera Theater, and the Georgian Museum of Fine Arts. A highlight is the Rustaveli State Academic Theater, a symbol of Georgias flourishing cultural scene. Be sure to explore the countless cafes, shops, and restaurants that pepper this avenue. Remember the 1989 April 9 tragedy, when a peaceful protest on this very avenue was met with Soviet force. Today, Rustaveli remains a site of public expression, while also hosting outdoor exhibitions and performances, reflecting the vibrant spirit of Tbilisi.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Rustaveli%20Avenue.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.693008585486,
  "Longitud": 44.8083227965416,
  "Monumento": "Peace Bridge",
  "Descripcion": "Welcome to the Bridge of Peace, a striking modern landmark in Tbilisis historic heart! Unveiled in 2010, this pedestrian bridge gracefully spans the Kura River, linking the Rike Park with the Old town. With its wavelike steel and glass design lit by thousands of LEDs, the bridge offers stunning views of Tbilisis iconic landmarks, such as the Metekhi Church and the Narikala Fortress. The mesmerizing interactive light display activates 90 minutes before sunset until 90 minutes after sunrise, with patterns that travel in waves, converge, and twinkle like stars. Walking along, youll notice motion sensors trigger the embedded LEDs in the railings, creating a personalised light show for every passerby. Despite some controversy over its futuristic design within the historical district, the Bridge of Peace has become a beloved symbol of Tbilisi, connecting its past with the present.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Peace%20Bridge.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.6930289259278,
  "Longitud": 44.8100563541626,
  "Monumento": "Rike Park",
  "Descripcion": "Welcome to Rike Park, a vibrant oasis in the heart of Tbilisi! This modern recreational area, shaped like a largescale map of Georgia, lies on the left bank of the Kura River. Accessed via the remarkable Bridge of Peace, or the steps from Avlabari, its a hub of activity. Here, youll find a dynamic mix of architectural wonders and familyfriendly attractions, from a giant chess board to a grand white piano. The park is beautiful at night when thousands of LEDs illuminate the river and surrounding buildings. The musicplaying fountain adds to the charm. Rike Park is also the starting point for the cable car ride up to the Narikala Fortress. Whether youre strolling through landscaped gardens, viewing art displays, or tasting traditional cuisines during Tbilisoba in October, Rike Park promises memorable moments!",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Rike%20Park.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.696057253986,
  "Longitud": 44.8002341422377,
  "Monumento": "The National Museum of Georgia",
  "Descripcion": "Welcome to the Georgian National Museum, a unified network of Georgias paramount museums, established in 2004. This exceptional institution provides a deep dive into the countrys history, from prehistoric animal remains from 40 million years ago to the most stunning artifacts of human existence outside Africa dating back 1.8 million years. The collection of Treasures, featuring unique gold and silver artifacts from the preChristian period, is truly aweinspiring. The network includes notable branches like the Simon Janashia Museum of Georgia, the Open Air Museum of Ethnography, the Museum of the Soviet Occupation, and more. Each visit promises a captivating journey through Georgias rich and diverse history.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/The%20National%20Museum%20of%20Georgia.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.6948554573842,
  "Longitud": 44.7825314900541,
  "Monumento": "Mtatsminda Park",
  "Descripcion": "Welcome to Mtatsminda Park, a picturesque park perched atop Mount Mtatsminda in Tbilisi. Founded by the Soviet government in the 1930s, the park was once among the most visited in the USSR. Today, it offers a variety of thrilling rides such as carousels, water slides, a rollercoaster, and a fascinating dark ride, the Ghost Castle. Dont miss the 65meterhigh Ferris Wheel, from where you can enjoy a splendid view over Tbilisi. The park is accessible via a funicular, an attraction in itself. Despite its complex history involving property seizures and a transformation into a modern theme park by Georgian billionaire Badri Patarkatsishvili, the park is now a beloved recreational spot in Tbilisi.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Mtatsminda%20Park.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.6949366047147,
  "Longitud": 44.7867526560659,
  "Monumento": "Funicular Restaurant Complex",
  "Descripcion": "Embark on a journey to the Funicular Restaurant Complex, situated at the peak of the Mtatsminda mountain in Tbilisi. Located within Mtatsminda Park, this culinary gem stands 800 meters above the city, boasting an unsurpassed view of Tbilisi. The complex, dating back to 1905, is undoubtedly one of the citys most significant places. Here, you can savor a blend of delicious food and drink in the most stylish setting, all while enjoying a panoramic view that French botanist Emil Levie likened to the sight of Paris from the top of the Eiffel Tower. Come experience the magic yourself!",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Mtatsminda%20Park.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.700958664064,
  "Longitud": 44.7959920776309,
  "Monumento": "Tbilisi Opera and Ballet Theatre",
  "Descripcion": "Immerse yourself in the world of opera and ballet at Tbilisis Georgian National Opera and Ballet Theater, a significant cultural icon since 1851. Standing on Rustaveli Avenue, this striking Moorish Revival edifice was conceived by architect Victor Schröter, inviting the city to experience a synthesis of Oriental charm and European grandeur. Despite several fires, it rose from the ashes each time, most recently rejuvenated in 2016. The theater has hosted worldrenowned performers, including Georgian composer Zacharia Paliashvili and ballet dancer Nina Ananiashvili. It continues to stage Georgianlanguage performances and globallyacclaimed operas. A visit here is a step back in time, a celebration of Georgias resilience and dedication to arts and culture.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Tbilisi%20Opera%20and%20Ballet%20Theatre.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.6904869058262,
  "Longitud": 44.8084378221245,
  "Monumento": "Chardin Street",
  "Descripcion": "Welcome to Chardin Street! Nestled in the bustling district of Upper Kala, this vibrant area is a true embodiment of Tbilisis captivating spirit. Originated in the 19th century, the street was formerly known as Dark Row due to its dense cluster of shops and workshops. Today, Chardin Street is a popular haunt filled with art galleries, souvenir shops, and a hint of modern architecture. It owes its name to Jan Chardin, a French explorer who visited in 1863. As you stroll along, youll encounter a small square and park adorned with the bronze Tamada statue, a symbol of Georgian hospitality, discovered in ancient Vani. Lastly, dont forget to visit the nearby historic Sioni Cathedral and old caravanserais.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Chardin%20Street.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.6955452228251,
  "Longitud": 44.8067742995262,
  "Monumento": "Anchiskhati Basilica",
  "Descripcion": "Welcome to the Anchiskhati Basilica of St Mary, Tbilisis oldest surviving church dating back to the 6th century. Established by King Dachi of Iberia, the basilica became home to the treasured 12thcentury icon of the Savior in 1675, now residing at the Art Museum of Georgia. Over centuries, the basilica underwent several transformations, most notably in the 1870s when a dome was added. A symbol of resilience, the basilica, despite periods of turmoil and secular use, was restored to its 17thcentury appearance in 1964, and religious use resumed in 1991. Marvel at the basilicas unique architecture  a threespan design with entrances on three sides and admire the 19thcentury paintings that adorn its interior. Dont miss out on the performances by the Anchiskhati Choir, renowned for their Georgian polyphonic choral music.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Anchiskhati%20Basilica.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.701011852537,
  "Longitud": 44.80310216549,
  "Monumento": "Dry Bridge Market",
  "Descripcion": "Welcome to the Dry Bridge Market, the beating heart of Tbilisi! Since its inception during the postcommunist dark 90s, this vibrant, openair flea market has transformed into an intriguing tourist hotspot. Youll find it set on the Dry Bridge, no longer over water, but over a street. Browse the four sections: the flea market for a nostalgic walk through Soviet history, the art & crafts market for unique handmade items, the antiques market for a hidden treasure trove of retro items, and the book market, a peaceful riverside respite for book lovers. Come on weekends for the liveliest atmosphere, and remember to bring cash. From Soviet kitsch to authentic Georgian crafts, this market captures Georgias rich and complex past in a fun and accessible way. Dont miss the nearby cafes for a gastronomic end to your market exploration!",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Dry%20Bridge%20Market.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.6867607205064,
  "Longitud": 44.8037001917467,
  "Monumento": "Botanical Garden",
  "Descripcion": "Welcome to the National Botanical Garden of Georgia, Tbilisis verdant gem. Dating back to at least 1625, it brims with over 3500 species of plants spread over 97 hectares. Once royal gardens, the area was renamed as Tbilisi Botanical Garden in 1845. Its not just about the flora, though. Its also home to historical landmarks, including the grave of the famed Azerbaijani writer Mirza Fatali Akhundov. Besides the botanical treasures, you will find a beautifully preserved 1909 tunnel, once Georgias largest nightclub Gvirabi. Renowned scientists like Yuri Voronov have contributed to its development, enhancing its scientific and aesthetic importance. Today, the garden is a bustling scientific hub, housing six research departments and a nursery. If youre visiting Tbilisi, dont miss out on this harmonious blend of natural beauty and historical intrigue.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Botanical%20Garden.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.7094459108325,
  "Longitud": 44.8029016815926,
  "Monumento": "Fabrika Tbilisi",
  "Descripcion": "Welcome to Fabrika, Tbilisis hotspot for creatives, where an abandoned Sovietera sewing factory transformed into a buzzing cultural center. Home to artists, innovative businesses, cafes, and the regions largest hostel, Fabrika is a beacon of revitalization and creativity. Its bare walls and raw surfaces echo its industrial past, with the vibrant street art adorning the facade, and a welcoming courtyard stands as a trendy social hub. This architectural marvel is situated in a historic district that, thanks to Fabrika, is now a popular artistic and hipster haven. You can cocreate, learn, socialize, or even have a sleepover here. Amidst the exciting hustle and bustle of Fabrika, youll experience a unique blend of authenticity, innovation, and cultural diversity.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Fabrika%20Tbilisi.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.6880041598758,
  "Longitud": 44.8111571078598,
  "Monumento": "Abanotubani",
  "Descripcion": "Discover Abanotubani, Tbilisis ancient district known for its unique sulphuric baths. Nestled at the foot of Narikala fort and on the Mtkvari Rivers eastern bank, this neighborhood holds a cherished place in Georgian history. As per legend, King Vakhtang Gorgasalis falcon discovered the hot springs here, leading to the foundation of Tbilisi. With architectural influences from the 17th and 18th century Iran, the baths are a sight to behold. They also offer more than just healing; they were once social hubs for feasts and relaxation. Dont miss this quintessential experience when in Tbilisi!",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Abanotubani.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.6902470984833,
  "Longitud": 44.7997351494906,
  "Monumento": "The Writers House of Georgia",
  "Descripcion": "Welcome to the Writers House of Georgia, a captivating Art Nouveau mansion located in Sololaki, Tbilisi. Constructed by entrepreneur David Sarajishvili between 19031905, its an architectural marvel combining neoBaroque elements. A hub for Georgian literature, its a place where famed literary group the Blue Horns convened in the early 1920s. The House experienced a significant renewal in 2008 and now hosts important literary events and even a restaurant in its garden during summer. Its 2017launched residency program and the Museum of Repressed Writers, opened in 2021, provide rich insight into Georgias literary history. A mustvisit for literature lovers!",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/The%20Writers%20House%20of%20Georgia.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.7158792843991,
  "Longitud": 44.7944132557456,
  "Monumento": "Art Palace",
  "Descripcion": "Welcome to the Art Palace of Georgia, located in the heart of Tbilisi on Kargareteli Street. Built as a symbol of love by Duke Constantine Petrovich of Oldenburg for Agrippina Japaridze, this architectural masterpiece combines elements of Gothic and Islamic architecture. Previously known as the Georgian State Museum of Theater, Music, Cinema and Choreography, the museum now holds a vast collection of over 300,000 items, detailing the evolution of Georgian scenic design, theatre, cinema, and more. The palace also houses Persian, Russian, and Western European fine art. Dont miss the ancient mask from the town of Vani. Open from Tuesday to Sunday, its a mustsee for art and history lovers!",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Art%20Palace.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.6913475215854,
  "Longitud": 44.8075065846538,
  "Monumento": "Sioni Cathedral",
  "Descripcion": "Welcome to the Sioni Cathedral of the Dormition! A historic jewel of Tbilisi, its name honors Mount Zion in Jerusalem. Founded in the 6th century and rebuilt numerous times, the Cathedral stands as a testament to Georgias rich history and resilience. Explore the intriguing blend of architectural styles, from its 13thcentury structure to 17th19thcentury renovations. Inside, discover mesmerizing murals painted by Russian artist Grigory Gagarin and a stone iconostasis from the 1850s. Dont miss the sacred Grapevine cross, believed to be crafted by Saint Nino herself. Once the main Georgian Orthodox Cathedral, it served as the publication site for the Russian Imperial manifesto on Georgias annexification. Despite its tumultuous history, it has stood defiantly through the ages and even functioned during Soviet times.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Sioni%20Cathedral.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.7705778841736,
  "Longitud": 44.8104427684807,
  "Monumento": "The Chronicle of Georgia",
  "Descripcion": "The Chronicle of Georgia, a monument located near the Tbilisi Sea, is a testament to Georgias rich history. Created by Zurab Tsereteli in 1985, it is an unfinished masterpiece composed of 16 towering pillars. The monuments top half showcases Georgian kings, queens, and heroes, while the bottom half narrates tales from Christs life. Youll also see St. Ninos grapevine cross and a chapel. The monument provides a stunning overview of Tbilisi and is near the Tbilisi Sea, a popular local attraction. Though its less frequented by tourists due to Tbilisis myriad of attractions, it offers an unparalleled insight into Georgias past.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/The%20Chronicle%20of%20Georgia.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.7043966276724,
  "Longitud": 44.7443474412313,
  "Monumento": "Ethnography Museum",
  "Descripcion": "Welcome to the Giorgi Chitaia Open Air Museum of Ethnography in Tbilisi, Georgia. This museum, founded by ethnographer Giorgi Chitaia in 1966, offers a splendid display of folk architecture and craftwork from across the country. Spanning 52 hectares, the museum houses 70 buildings and over 8,000 items, each telling a unique story of Georgias rich cultural heritage. Experience the eastern Georgian darbazitype stone houses, western Georgian wooden houses with gable roofs, traditional watchtowers, wineries, water mills, and a collection of traditional household articles. The museum also hosts the annual ArtGene folk culture festival, providing a vibrant showcase of Georgian folk art and music.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Ethnography%20Museum.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.697259688057,
  "Longitud": 44.7995811495437,
  "Monumento": "Fine Art Museum of Georgia",
  "Descripcion": "Welcome to the Fine Art Museum of Georgia, an artistic treasure house showcasing an array of Georgian, Oriental, Russian, and European art. The museum, founded in 1920 and named after art historian Shalva Amiranashvili, harbors over 140,000 art pieces. Marvel at the Georgian art collection, illustrating the nations artistic evolution from ancient times to present. Dont miss the Oriental section, one of the largest in postSoviet countries, spotlighting the fine art of the Persian Qajar era. Make sure to visit special exhibitions frequently held to display artworks from diverse collections.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Fine%20Art%20Museum%20of%20Georgia.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.6979770744988,
  "Longitud": 44.7992856895927,
  "Monumento": "Kashveti Church of St. George",
  "Descripcion": "Welcome to the stunning Kashveti Church of St. George! A masterful blend of Georgian, Italian, and German influences, this Georgian Orthodox Church stands across the Parliament building in the heart of Tbilisi. Constructed from 1904 to 1910, its architecture echoes the medieval Samtavisi Cathedral. Breathtaking frescoes by celebrated Georgian artist Lado Gudiashvili adorn the interior, illustrating Christian stories with ancient encaustic techniques. A site of deep historical and religious significance, Kashveti takes its name from an old legend featuring the 6thcentury monk, David of Gareja, who proved his innocence against false accusations by causing a woman to give birth to a stone. This story, reflected in the churchs name, weaves faith, history, and miracles together, attracting believers and tourists alike.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Kashveti%20Church%20of%20St.%20George.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.7454798282671,
  "Longitud": 44.7383901587073,
  "Monumento": "Lisi Lake",
  "Descripcion": "Welcome to Lisi Lake, an oasis of serenity just outside Tbilisi, Georgia. This small lake in the Kura River Valley, known for its rocky terrain and diverse ecosystem, is home to exotic birds, turtles, foxes, and even a large population of snakes. An intriguing feature of Lisi Lake is the Green Lisi Town project, a mixeduse development designed by Andropogon, brought to life by TBC Bank Chairman Mamuka Khazaradze. Enjoy the Mediterranean climate as you stroll around the lake, but remember, the controversial history of its redevelopment continues to stir debates.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Lisi%20Lake.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.6893214258636,
  "Longitud": 44.8092871948609,
  "Monumento": "Meidan District",
  "Descripcion": "Welcome to Meidan, the beating heart of Old Tbilisi, bustling with history and life. Explore characteristic architecture, take a relaxing dip in sulfur baths, marvel at the bluemosaic mosque, and experience the tranquility of Leghvtakhevi Waterfall. From Meidan, gaze upon the Metekhi Temple and Narikala Fortress. Stop by the numerous cafes and shops, taste traditional Georgian dishes, and shop for items inspired by Georgian culture. Dont miss the St. George Armenian Cathedral, home to SayatNovas tomb, and the nearby Botanical Garden.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Meidan%20District.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.7034811103736,
  "Longitud": 44.7912533416479,
  "Monumento": "House of MelikAzaryants",
  "Descripcion": "Visit the House of MelikAzaryants, an iconic monument on Tbilisis central Rustaveli Avenue. This stunning edifice, built in the Art Nouveau style, represents an architectural gem from the early 20th century. Marvel at the stonecarved garlands, Czech sculptural reliefs, and traditional Tbilisian wooden balconies adorning the building. This house, built on a former landfill, was a progressive multipurpose complex of its time, boasting hotel rooms, shops, a photo salon, preschool, cinema, and an art gallery. The House of MelikAzaryants tells a poignant tale of the owners loss, reflected in its ascetic appearance, tearshaped windows, and funeral wreaths.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/House%20of%20MelikAzaryants.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.6902346381274,
  "Longitud": 44.8111712656997,
  "Monumento": "Assumption Church of Metekhi",
  "Descripcion": "The Virgin Mary Assumption Church of Metekhi, also known as Metekhi Church, is a key Georgian Orthodox Christian site in Tbilisi, dating back to the 13th century. Perched on the Metekhi Cliff, the church offers a breathtaking view of the old town across the Kura river. Its unique architecture, with three convex apses and a dome held internally by four pillars, make it a significant historical monument. The churchs stone walls are adorned with intricate rock carvings, a testimony to Georgias Golden Age. Metekhi also has a tragic history, notably the event of 1226, when around 100,000 citizens were executed for refusing to step on holy icons. Today, the church continues to be a place of worship and a fascinating historical site for tourists.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Assumption%20Church%20of%20Metekhi.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.6962134417742,
  "Longitud": 44.8066787517345,
  "Monumento": "Animated Puppet Museum",
  "Descripcion": "Discover a whimsical world of art and tradition at the Animated Puppet Museum in Tbilisi. Home to over three thousand exhibits, including dolls in traditional Georgian attire, the museum reflects a blend of creativity, culture, and craftsmanship. Founded in the 1930s by Tamar Tumanishvili, a childrens author and teacher, the museum boasts an eclectic mix of dolls, mechanical toys, and unique embroideries from 40 different countries. These exhibits are the result of eight decades of dedication from artists, collectors, and toy factories alike. Experience the captivating tales of Georgian folklore through these inanimate yet expressive characters. Situated at Agmashenebeli Avenue 103, the museum is open every day from 10:00 to 18:00, except Mondays.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Animated%20Puppet%20Museum.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.7218865861882,
  "Longitud": 44.7882198086207,
  "Monumento": "Silk Museum",
  "Descripcion": "Delve into the history and craft of silk production at the Georgian State Silk Museum. Established in 1887 by Russian biologist Nikolay Shavrov, it is one of the oldest and few sericulture museums globally. Housed in a building designed by 19thcentury Polish architect Alexander Szymkiewicz, the museum holds an impressive collection of 40,000 objects from 61 countries. Here, youll find everything from cocoons and textiles to natural dyes, old photographs, and objects related to silkmaking. With displays detailing the biology of silkworms, the tools used in silk laboratories, and an ethnographic collection, the museum offers an insightful journey through the history and techniques of sericulture.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Silk%20Museum.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.7501566350027,
  "Longitud": 44.8416667876212,
  "Monumento": "Tbilisi Sea",
  "Descripcion": "Take a break from city life at Tbilisi Sea, an artificial reservoir created in 1951 during the Soviet era. Originally intended for irrigation, this beautiful spot is now a hub for water sports, boating, and swimming. Bask in the serene surroundings, or make your way to the Chronicles of Georgia, a monumental creation by sculptor Zurab Tsereteli that depicts important Georgian historical events and literary works. On the shores, youll find Gino Paradise, a toptier water park, wellness and sportsrecreation center. Dont miss the breathtaking views from the Holy Mother of God Church, located behind the monuments, offering a panorama of Tbilisi districts and the sea.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Tbilisi%20Sea.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.700451297241,
  "Longitud": 44.7541071602983,
  "Monumento": "Turtle Lake",
  "Descripcion": "Welcome to Turtle Lake, or Kus Tba, a charming small lake nestled on the outskirts of Tbilisi, Georgia. Positioned 686.7 m above sea level, on the northern slope of the Mtatsminda ridge, it provides a tranquil retreat from the city buzz. Come summer, the lake transforms into a hub for sports events and swimming. You can enjoy openair cafes, a minifootball stadium, and a childrens playground. Turtle Lake is also the home to an openair ethnographic museum, showcasing Georgia in miniature. Recently, a new ropeway system was introduced, making access even easier from the city center. Fun fact: in 2016, Gambusia fish were introduced into the lake to combat the mosquitoes spreading the Zika virus.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Turtle%20Lake.jpg"
 },
 {
  "Pais": "Georgia",
  "Ciudad": "Tbilisi",
  "Latitud": 41.6961939477065,
  "Longitud": 44.7991557867439,
  "Monumento": "Vorontsov Palace",
  "Descripcion": "Welcome to the Vorontsov Palace, a gem of Tbilisi that reflects a critical chapter in Georgias history. Built in 1868 by Governor Mikhail Vorontsov, this Renaissancestyle edifice stands proudly on Rustaveli Avenue. Its elegant decor and sublime beauty rival the finest European architecture. Inside, youll be enthralled by the splendor of the Persian hall, an ethereal room where mirrors amplify the lightness and purity of the white decorations. Vorontsovs tenure brought progress to Georgia, yet the Palaces legacy doesnt stop there. The birth of independence for Georgia, Armenia, and Azerbaijan echoed within its walls. Today, it serves as the Youth Palace, continuing to contribute to Georgian society. Its historical significance, breathtaking beauty, and continuous relevance make it a mustvisit for every tourist.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_tbilisi/Vorontsov%20Palace.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Lima Center",
  "Latitud": 12.0459749728434,
  "Longitud": 77.0305310188497,
  "Monumento": "Plaza de Lima",
  "Descripcion": "The Plaza de Armas de Lima, or Plaza Mayor, is the founding site of Lima, Perus capital. A central public space in the historical heart of the city, it is bordered by the Government Palace, Lima Cathedral, and other notable buildings. Established in 1535 by Francisco Pizarro, its a fusion of history and architectural brilliance, with the plaza playing host to numerous significant events, including Perus proclamation of independence in 1821.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_lima/Plaza%20de%20Lima.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Lima Center",
  "Latitud": 12.0467130882372,
  "Longitud": 77.0297079638355,
  "Monumento": "Cathedral of Lima",
  "Descripcion": "The Cathedral of Lima, officially known as the Catedral Basílica San Juan Apóstol y Evangelista, stands proudly in Limas historic center. Originally built on an ancient Incan site, its foundation was laid by Francisco Pizarro in 1535. Over the centuries, the cathedral underwent several reconstructions due to earthquakes and changing architectural styles. Today, its a blend of baroque, gothic, neoclassical, and romantic elements. Recognized as a UNESCO World Heritage site since 1991, it remains an essential visit for anyone touring Peru.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_lima/Cathedral%20of%20Lima.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Lima Center",
  "Latitud": 12.045104581501,
  "Longitud": 77.0299724228948,
  "Monumento": "Presidential Palace",
  "Descripcion": "The Government Palace, also known as the House of Pizarro, is the official residence of the president of Peru and the seat of the executive branch. Located in Limas Plaza Mayor, it stands on an ancient indigenous site and was first constructed by Francisco Pizarro in 1535. Throughout its history, the building has been renovated multiple times, with the current NeoPlateresque design stemming from the 1920s. The palace is also famous for its daily Changing of the Guard ceremony, a key attraction for visitors.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_lima/Presidential%20Palace.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Lima Center",
  "Latitud": 12.0444525356616,
  "Longitud": 77.0287776200823,
  "Monumento": "Desamparados Station",
  "Descripcion": "The Desamparados station in Lima, Peru, stands beside the Government Palace, named after the church of Nuestra Señora de los Desamparados. Today, it mainly serves as an exhibition hall, housing the presidential wagon Paquita. Built in 1912 by the Peruvian architect Rafael Marquina, it showcases BeauxArts architecture and a stunning Art Nouveau stained glass skylight.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_lima/Desamparados%20Station.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Lima Center",
  "Latitud": 12.0454602782401,
  "Longitud": 77.0272300078309,
  "Monumento": "San Francisco Convent",
  "Descripcion": "The Basilica and Convent of San Francisco, situated in the heart of Lima, represents an architectural masterpiece from the viceroyalty era. Famous for its Liman Baroque style facade and Neoclassical main altar, the complex boasts an impressive library, intricately designed choir stalls, and mysterious catacombs housing up to 70,000 individuals. Visitors can also admire the San Francisco main cloisters collection of paintings depicting Saint Francis of Assisis life, revealing a rich tapestry of history and art.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_lima/San%20Francisco%20Convent.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Lima Center",
  "Latitud": 12.051642354833,
  "Longitud": 77.034627618737,
  "Monumento": "Plaza San Martin",
  "Descripcion": "Plaza San Martín, situated at the heart of Limas UNESCOrecognized Historic Centre, is an iconic representation of the citys rich heritage. Not only does its central monument honor Perus liberator, Jose de San Martín, but the plaza itself is a testament to Limas evolution, from its days as a hospital to a railway station, and finally, the magnificent plaza inaugurated in 1921. Visitors will appreciate the cohesive baroque architectural style, especially the neocolonial facades of the surrounding buildings, though some, like the Giacoletti and Marcionelli buildings, have tragically been affected by fires in recent years.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_lima/Plaza%20San%20Martin.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Lima Center",
  "Latitud": 12.0704330676362,
  "Longitud": 77.0351799896894,
  "Monumento": "Water Park of the Reserve",
  "Descripcion": "Limas Park of the Reserve, situated in the Santa Beatriz neighborhood, is a tribute to reservist troops from the Pacific War. Founded in 1926, the park showcases neoclassical design and features the Magic Water Circuit  the worlds largest fountain complex in a public park, recognized by the Guinness World Records.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_lima/Water%20Park%20of%20the%20Reserve.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Lima Center",
  "Latitud": 12.1236430601285,
  "Longitud": 77.0401687781218,
  "Monumento": "Lighthouse of Miraflores",
  "Descripcion": "Miraflores Lighthouse, perched over the Pacific Ocean in Limas Miraflores district, is an iconic and frequently visited beacon. Constructed by the Chance Bros of Sweden in 1900, it boasts an impressive 22meter height and a light visible up to 21 miles away. Contrary to urban legends, it wasnt designed by Gustave Eiffel.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_lima/Lighthouse%20of%20Miraflores.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Lima Center",
  "Latitud": 12.111167680943,
  "Longitud": 77.0332701259625,
  "Monumento": "Huaca Pucllana",
  "Descripcion": ":Huaca Pucllana, located in Miraflores, Lima, is an ancient archaeological site belonging to the Lima culture (200  700 AD). After years of neglect, its been conserved since 1981 and is now a major tourist attraction in Lima. Featuring adobe construction, it consists of a 25meter high pyramid and various patios and enclosures. Known for its iconic bookshelf technique architecture, Huaca Pucllana was a ceremonial center with significant marinethemed ceramics. Today, the site showcases Limas history and its artistic importance, from religious rituals to elite burials.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_lima/Huaca%20Pucllana.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Lima Center",
  "Latitud": 12.0873465669804,
  "Longitud": 77.0015008856704,
  "Monumento": "National Museum",
  "Descripcion": "The Museo de la Nación in Lima, Peru, is a pivotal landmark celebrating Perus rich tapestry of history and art. Located within the Ministry of Culture building, the museum boasts an impressive collection of 15,500 works, primarily from the preHispanic era. Notable for its archaeological, historical, and ethnographic exhibits, its a mustvisit for those keen on immersing in Perus cultural legacy. Check for rotating temporary exhibits and live cultural performances to complete your experience.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_lima/National%20Museum.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Lima Center",
  "Latitud": 12.0599345153469,
  "Longitud": 77.1462910436565,
  "Monumento": "Monumental Callao",
  "Descripcion": "Monumental Callao is a vibrant art hub in the historic district of Callao, Lima. Founded in 1537, this once neglected port district has been rejuvenated into a bustling locale of art, music, and gastronomy. Highlights include the multifaceted “Casa Fugaz”, offering galleries, boutiques, and a stunning terrace view of the harbor. Explore the areas dynamic art scene or relax at the top floor parties on Saturdays.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_lima/Monumental%20Callao.jpg"
 },
 {
  "Pais": "Peru",
  "Ciudad": "Lima",
  "Distrito": "Lima Center",
  "Latitud": 12.0971541601345,
  "Longitud": 77.0405674431398,
  "Monumento": "Huaca Huallamarca",
  "Descripcion": "The Huaca Huallamarca, once named Pan de Azúcar, stands as a truncated steppyramid rising to about 19 meters in Limas San Isidro district. This preHispanic construction dates back to 200 A.D., serving first as a ceremonial temple and later as a cemetery. Over the years, its been the focal point for various cultures like Lima, Huaura, Sicán, Chincha, and Ychsma. Today, amidst modern skyscrapers, it offers a contrasting glimpse into Perus preColumbian era.",
  "Imagen": "https://www.wagnerproducciones.com/travelmeit/monumentos_lima/Huaca%20Huallamarca.jpg"
 }
]
"""
        sites_json = json.loads(sites)

        return Response(
            sites_json, 
            status=status.HTTP_200_OK, 
            content_type="application/json"
        )

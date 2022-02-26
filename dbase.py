from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('postgres://bbcrruoboyjxbw:e254c3465ba888c6aad0a1af42433f148c8dea1b4c115bd6dd0056eab958e9a8@ec2-54-237-155-151.compute-1.amazonaws.com:5432/ddps5i5qa1eukt',echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class leaf(Base):
	__tablename__ = 'leaf_database'
	id = Column(Integer, primary_key = True)
	leaf_name = Column(String(100))
	med_use = Column(String(1000))
	place = Column(String(100))
	nut_cont = Column(String(1000))
	other_name = Column(String(1000))
	season = Column(String(1000))
	soil_condi = Column(String(1000))
	other_use = Column(String(1000))
	scien_name = Column(String(1000))
	charac = Column(String(1000))
	side_effects = Column(String(1000))


Base.metadata.create_all(engine)

obj1 = leaf(leaf_name="Pubescent Bamboo", 
			med_use="It is used to treat Respiratory disorders, Asthma, Coughs and Gallbladder disorders.",
			place="China and Taiwan", 
			nut_cont = " Thiamine, Niacin, Vitamin A, Vitamin B6, Vitamin E", 
			other_name = "Guadua Bamboo", 
			season = "April to June", 
			soil_condi = "Plant grows efficiently in moist, but well-drained soil in a sheltered, sunny spot. These bamboo will grow in poor soils, but not in constant wet, boggy or extremely dry conditions.", 
			other_use = "It is also used for building roads,make clothes.,accessories and scaffolding", 
			scien_name = "Phyllostachys edulis", 
			charac = "The outer layer of the stem is quite dense and strong. Bamboo is both flexible and elastic. As a result items made from bamboo tend to be very resilient and resist breaking when placed under stress",
			side_effects = "Reported side effects is people with thyroid disorders, such as goitre, hypothyroidism, and thyroid tumour, are not advised to consume bamboo. Since there is a lack of details regarding the extent of its safety, pregnant and breastfeeding mothers should avoid bamboo supplementation.")

obj2 = leaf(leaf_name = "Chinese horse chestnut",
			med_use = "It is used to treat Circulatory problems, Astringent, Diuretic and to reduce Inflammation.",
			place = "Northern China",
			nut_cont = "Glucose, Vitamin C",
			other_name = "Chinese buckeye, Aesculus chinensis",
			season = "March to June", 
			soil_condi = "Plant grows efficiently in USDA plant hardiness zones 3-8 in areas having full sun and well-drained, but moist, humus-rich soil. These trees do not tolerate excessively dry conditions.", 
			other_use = "It is also used for chestnut is a nutrient-dense food and contains high amounts of fibre, potassium, manganese, copper, vitamin B6 and riboflavin. Most of their calories come from their god carb content.", 
			scien_name = "Aesculus hippocastanum", 
			charac = "The bark is grayish-green or grayish-brown in color, and the tree limbs are thick and have corky and the interior of horse chestnut bark is pinkish-brown, with fine lines running its length",
			side_effects = "Reported side effects is seed extract are mild and include digestion issues, upset stomach, dizziness, headache, and itching.")

obj3 = leaf(leaf_name = "Anhui Barberry",
			med_use = "It is used to treat Diabetes, Liver disease and to promote good Dental health and in Cancer treatment and prevention.",
			place = " Europe, North America.",
			nut_cont = "Vitamin C, Iron",
			other_name = "Berberis vulgaris, Barberry",
			season = "March to November", 
			soil_condi = "Plant grows efficiently in full sun or partial shade and are very adaptable to a wide range of soil types as long as it drains well", 
			other_use = "It is also used for preparing an antioxidant.", 
			scien_name = "Berberis microphylla", 
			charac = "Leaves grow in clusters on arched hanging branches. Small, toothed, ovate, alternate, dull green above and grayish below. On young sprouts they are spiny.",
			side_effects = "Reported side effects on the heart/blood vessel system (eg, low blood pressure, decreased heart rate) and decreased breathing may occur with high  dosages")

obj4 = leaf(leaf_name = "Chinese redbud",
			med_use = "It is used as an Antiseptic, treats Bladder diseases, Postpartum discharges, bleeding piles and internal parasites.",
			place = "Central China",
			nut_cont = "Proteins, Fat",
			other_name = "Cercis chinensis, Weaver's shuttle, Judas-tree",
			season = "March to June", 
			soil_condi = "Plant grows efficiently in acidic, alkaline, loamy, moist, rich, sandy, well-drained and clay soils.", 
			other_use = "It is also be pickled and used as a caper substitute, and can add a bright, citrusy taste to salads. .", 
			scien_name = "Cercis chinensis", 
			charac = "These are rosy-purple flower clusters, long purple seed pods, and round, glossy leaves that taper to a point",
			side_effects = "Reported side effects is that it contain a toxic saponin. Although toxic, saponins are poorly absorbed by the body and most pass straight through without any problem. They are also broken down to a large extent in the cooking process.")

obj5 = leaf(leaf_name = "true indigo",
			med_use = "It is used to detoxify the blood, reduce inflammation and clean the liver.",
			place = "South-east areas",
			nut_cont = "Vitamin C, Iron and have a high calorific value.",
			other_name = "Tinctoria, Indigofera tinctoria",
			season = "Early February and mid-April.", 
			soil_condi = "Plant grows efficiently in zones 9 and warmer, but in colder climates it will grow as an annual. Growing indigo from seed is not difficult, but it does require warmth. If you are not in a warm climate,", 
			other_use = "It is also used for indigo is as a dye for cotton yarn, blue jeans. Small amounts are used for dyeing wool and silk.", 
			scien_name = "Indigofera tinctoria", 
			charac = "Indigo species are highly variable in appearance but are generally silky or hairy with compound leaves. The rose, purple, or white flowers are borne in showy spikes or clusters, and the fruit is a pod, usually with a thin partition between the seeds.",
			side_effects = "Reported side effects is powder allergy are itchiness, headache and dizziness.")

obj6 = leaf(leaf_name = "Japanese maple",
			med_use = "It is used to treat Rheumatism, Bruises, Hepatic disorders and  Eye disease. ",
			place = "East Asia and North America",
			nut_cont = "Low foliar nutrient content",
			other_name = "Acer palmatum, Palmate maple",
			season = "September and October", 
			soil_condi = "Plant grows efficiently in acidic conditions, where they pair beautifully with Rhododendrons, Camellias, and Kalmias. But they are also perfectly content in neutral and even mildly alkaline pH.", 
			other_use = "It is also used for homes, shelter and food for wildlife. Leaves feel similar to paper and are used to make bouquets.", 
			scien_name = "Acer palmatum", 
			charac = "Leaves of the species form are oppositely arranged, hand-shaped, 2 to 5 inches long and have 5 or 7 lobes. Summer color is green and autumn color varies from orange to yellow to red to purple.",
			side_effects = "No side effects is reported")

obj7 = leaf(leaf_name = "Nanmu",
			med_use = "It is used to treat Stomach diseases, Cholera and Tendons.",
			place = "Ledong, Hainan, China,",
			nut_cont = "High content of sugar, vitamin C",
			other_name = "Golden Thread Nanmu, Machilus nanmu",
			season = "All season", 
			soil_condi = "Plant grows efficiently in fertile soils in ravines and along rivers.", 
			other_use = "It is also used for boat building, architectural woodworking, furniture and sculptural carving. ", 
			scien_name = "Phoebe nanmu", 
			charac = "These can be as high as 30 meters, its leaves are oblong or narrow oval, grow about 5 to 11 cm, width about 1.5 to 4 cm, the apex of the leaves gradually become sharp, the base is wedge-shaped, the surface is shiny.",
			side_effects = "Reported side effects are vomiting, diarrhea, drowsiness, blood disorders, seizures, loss of consciousness, coma, brain disorders, and death. Pregnancy and breast-feeding: Neem oil and neem bark are LIKELY UNSAFE when taken by mouth during pregnancy.")
			
obj8 = leaf(leaf_name = "castor aralia ",
			med_use = "It is used to treat Contusions, Neuralgia, Rheumatic arthritis and Lower back pain.",
			place = "Korea",
			nut_cont = "Calcium, Magnesium, Zinc, Iron, and Beta-Carotene",
			other_name = "Prickly Castor oil tree, Aralia",
			season = "July and even August", 
			soil_condi = "Plant grows efficiently in full sun on well- drained soil and will tolerate alkaline soil. While drought-tolerant once established, Castor-Aralia should receive ample moisture until then.", 
			other_use = "Only medicinal purpose.", 
			scien_name = "Kalopanax septemlobus", 
			charac = "These are massive, spreading branches and large, 7- to 12-inch-diameter, dark green, multi-lobed leaves, Castor-Aralia provides dense shade below its canopy and makes an ideal shade tree. Growing 40 to 50 feet high with an equal spread,",
			side_effects = "Reported side effects are poisonous causing transitory muscle tremors, ataxia, and excessive salivation.")
                               
			
obj9 = leaf(leaf_name = "Cinnamon",
			med_use = "It is used to cut the risk of Heart disease and lowers Blood Sugar levels and has a powerful Anti-Diabetic effect.",
			place = "Vietnam and Indonesia",
			nut_cont = "Iron, Calories, Vitamin A",
			other_name = "Cinnamomum verum, Ceylon cinnamon",
			season = "April to June", 
			soil_condi = "Plant grows efficiently in a wide range of soils, from organic-rich loamy soils to poor sandy loam soils", 
			other_use = "It is also used for stimulate Hair Growth,Help Digestion & Heartburn,Treat Acne & Eczema", 
			scien_name = "Cinnamomum verum", 
			charac = "It is of a golden-yellow colour, with the characteristic odour of cinnamon and a very hot aromatic taste. The pungent taste and scent come from cinnamaldehyde (about 90 percent of the essential oil from the bark) and, by reaction with oxygen as it ages, it darkens in colour and forms resinous compounds.",
			side_effects = "Reported side effects are nausea, abdominal pain and rapid heart beat if you ingest too much.May Cause Low Blood Sugar and breathing problems.")
                               
			
obj10 = leaf(leaf_name = "Golden Rain Tree",
			med_use = "It is used to treat Conjunctivitis and Epiphora.",
			place = "Northern China and Korea",
			nut_cont = "Unsaturated fatty acid, Oleic acid, Eicosenoic acid, Erucic acid",
			other_name = "China tree, Varnish tree.",
			season = "April to June ", 
			soil_condi = "Plant grows efficiently in acidic, alkaline, loamy, sandy, well-drained, wet and clay soils. It has some drought tolerance.", 
			other_use = "Only medicinal purpose.", 
			scien_name = "Koelreuteria paniculata", 
			charac = "These are golden rain-tree, Koelreuteria paniculata, grows 30 to 40 feet tall with an equal spread in a broad vase or globe shape. ... Rain-tree bears large, beautiful panicles of bright yellow flowers in May and holds seed pods that look like brown Chinese lanterns.",
			side_effects = "Reported side effects is the seeds are legumes with large numbers of black seeds that contain cytisine, an alkaloid extremely poisonous to humans as well as goats and horses, especially when not ripe.")
                   			
obj11 = leaf(leaf_name = "Big-fruited Holly",
			med_use = "It is used to treat Alleviate Measles, Colds, Flu, and Pneumonia.",
			place = "Area, Europe, Asia, and Africa",
			nut_cont = "Vitamin C",
			other_name = "Ilex opaca",
			season = "December to January", 
			soil_condi = "Plant grows efficiently in moist, acidic, loose, well-drained soil. It will grow in sun or partial shade. This tree will not tolerate poorly drained areas, and will not perform well in dry, windy, unprotected sites.", 
			other_use = "Considered as a holy plant", 
			scien_name = "Ilex opaca", 
			charac = "These are genus have simple, alternate glossy leaves, frequently with a spiny leaf margin. The inconspicuous flower is greenish white, with four petals. They are generally dioecious, with male and female flowers on different plants.",
			side_effects = "Reported side effects are diarrhea, nausea, vomiting, and stomach and intestinal problems. Swallowing holly leaf spines may tear or puncture the inside of the mouth and other parts of the digestive tract.")
             			
obj12 = leaf(leaf_name = "Japanese cheesewood",
			med_use = "No medicinal use",
			place = "Japan, Korea and China",
			nut_cont = "Vitamin C",
			other_name = "Austrian laurel, Japanese Pittosporum, Mock Orange Mock, Orange Pittosporum.",
			season = "April to May", 
			soil_condi = "Plant grows efficiently in  Sun: Full sun to part shade Water: Medium", 
			other_use = "It is also used to make Shields that can shield a house from wind as well as provide Privacy and Toxic to animals.", 
			scien_name = "Pittosporum tobira", 
			charac = "It is an evergreen shrub which can reach 10 m (33 ft) tall by 3 m (10 ft) broad,[2] and can become treelike. It can also be trimmed into a hedge. The leaves are oval in shape with edges that curl under and measure up to 10 cm (4 in) in length.",
			side_effects = "Reported side effects is a poisonous compound is found in pittosporum, called saponin, that is especially toxic to animals.")                           
			
obj13 = leaf(leaf_name = "wintersweet",
			med_use = "It is used as a folk medicine in China for treating measles, coughs, tonsillitis and pharyngitis.",
			place = "Japan, Korea, Europe, Australia, and the United States",
			nut_cont = "Vitamin D",
			other_name = "Japanese Allspice",
			season = "November to March", 
			soil_condi = "Plant grows efficiently in  light (sandy), medium (loamy) and heavy (clay) soils and prefers well-drained soil,It cannot grow in the shade. It prefers moist soil.", 
			other_use = "It is also used for ornaments and fragrance..perfume", 
			scien_name = "Chimonanthus praecox", 
			charac = "It is a vigorous deciduous shrub growing to 4 m (13 ft) tall with an erect trunk and leaves 5–29 cm (2–11 in) long and 2–12 cm (1–5 in) broad. Its strongly scented pendent flowers, produced in winter (between November and March in UK,[4]) on bare stems, have 15-21 yellow or pale green-yellow, sepals, the inner ones usually with purplish red pigments",
			side_effects = "Reported side effects is toxicity due to ingestion of wintersweet, which contains the alkaloid calycanthine toxicity including ataxia, hyperaesthesia and seizures.")

obj14 = leaf(leaf_name = "camphor tree",
			med_use = "It is used to treat Skin diseases, improve Respiratory function, and relieve Pain and can also be used directly on hands and feet to treat Chilblains and to treat Acne and Cold sores.",
			place = "China and southern Japan",
			nut_cont = "Antibiotic",
			other_name = "True camphor, Laurel camphor, Japanese camphor.",
			season = "March to June", 
			soil_condi = "Plant grows efficiently in full sun or partial shade", 
			other_use = "It is also used for camphor and timber production.", 
			scien_name = "Cinnamomum camphora", 
			charac = "It grows up to 20–30 m (66–98 ft) tall.[2] In Japan, where the tree is called kusunoki, five camphor trees are known with a trunk circumference above 20 m (66 ft), with the largest individual",
			side_effects = "Reported side effects are possible to cause a rash or allergic reaction Children and pregnant or breastfeeding women should not use this herbs in some people.Overuse can cause skin irritation and no products containing camphor should be used on open wounds or burns. All internal uses of the herb are advised against.")
                               
obj15 = leaf(leaf_name = "Japan Arrowwood",
			med_use = "It is used to treat Snake bites, Dysentery, and Vermifuge",
			place = "China, Japan, and Korea",
			nut_cont = "Immunity booster",
			other_name = "Viburnum dilatatum, Linden Viburnum, Linden Arrowwood",
			season = "All season", 
			soil_condi = "Plant grows efficiently in grown in moist fertile soil that is slightly acidic or neutral", 
			other_use = "It is also used for ornamental plant", 
			scien_name = "Viburnum dilatatum", 
			charac = "The size of the leaf ranges from 5.1–13 centimetres (2.0–5.1 in) long and 2.5–6.4 centimetres (0.98–2.52 in) wide.[3][4][6] The leaves have shallowly toothed margins, usually are pubescent and they drop in late autumn.",
			side_effects = "Reported side effects is huge consumption may lead to dizziness")
                               
			
obj16 = leaf(leaf_name = "sweet osmanthus",
			med_use = "It is used to prepare Osmanthus tea has been used as an Herbal tea for the treatment of Irregular Menstruation",
			place = "Eastern Asia",
			nut_cont = "Rich source of Phytochemicals",
			other_name = "Osmanthus fragrans, Fragrant Tea Olive, Sweet Osmanthus, Tea Olive",
			season = "December to May", 
			soil_condi = "Plant grows efficiently Moist, Occasionally Dry soil.", 
			other_use = "It is also used for Buffer, Fragrance, Screening", 
			scien_name = "Osmanthus fragrans", 
			charac = "It is an evergreen shrub or small tree growing to 3–12 m (9.8–39.4 ft) tall. The leaves are 7–15 cm (2.8–5.9 in) long and 2.6–5 cm (1.0–2.0 in) broad, with an entire or finely toothed margin.",
			side_effects = "Reported side effects is hair weakness")
                               
			
obj17 = leaf(leaf_name = "Deodar",
			med_use = "It is used to make Cedar oil that is often used in aromatherapy.",
			place = " Afghanistan",
			nut_cont = "Calcium",
			other_name = "Cedrus deodara",
			season = "March to August", 
			soil_condi = "Plant grows efficiently in landscapes and hill stations", 
			other_use = "It is also used for ornaments for people", 
			scien_name = "Cedrus deodara", 
			charac = "It is a large evergreen coniferous tree reaching 40–50 m (131–164 ft) tall, exceptionally 60 m (197 ft) with a trunk up to 3 m (10 ft) in diameter. It has a conic crown with level branches and drooping branchlets.",
			side_effects = "Reported side effects is severe damage to health.1 leaf intake is advisable")                           

obj18 = leaf(leaf_name = "Ginkgo",
			med_use = "It is used to treat Anxiety and Depression,Schizophrenia and to cure insufficient Blood Flow to the brain.",
			place = "China",
			nut_cont = "Protein",
			other_name = "Ginkgo biloba, Maidenhair tree",
			season = "September to December", 
			soil_condi = "Plant grows efficiently in well-draining soil in an area of full to partial sun. Regular watering and a well balanced fertilizer regime is also recommended, at least until maturation.", 
			other_use = "Only for medicinal purpose.", 
			scien_name = "Ginkgo biloba", 
			charac = "These are large trees, normally reaching a height of 20–35 m (66–115 ft), with some specimens in China being over 50 m (160 ft). The tree has an angular crown and long, somewhat erratic branches, and is usually deep rooted and resistant to wind and snow damage.",
			side_effects = "Reported side effects is an allergic reaction in some people.,headache")

		
obj19 = leaf(leaf_name = "Maidenhair tree",
			med_use = "It is used to improve Brain function, reduce Anxiety and treat Depression",
			place = "China and Asia",
			nut_cont = "Protein",
			other_name = "Ginkgo biloba, Maidenhair tree",
			season = "September to Dcember", 
			soil_condi = "Plant grows efficiently in Hardiness Zones 3–8.,The ginkgo grows in acidic, alkaline, loamy, moist, rich, sandy, silty loam, well-drained, wet and clay soils. It tolerates moderate drought and wetness but doesn’t grow well in hot, dry climates.", 
			other_use = "It is also used in commercial medicines for cognitive complaints such as Alzheimer's.", 
			scien_name = "Ginkgo biloba", 
			charac = "These are large trees, normally reaching a height of 20–35 m (66–115 ft), with some specimens in China being over 50 m (160 ft). The tree has an angular crown and long, somewhat erratic branches, and is usually deep rooted and resistant to wind and snow damage.",
			side_effects = "Reported side effects is an allergic reaction in some people.,headache")

obj20 = leaf(leaf_name = "Crape myrtle",
			med_use = "It is used to treat Diabetes and regulates Blood Pressure, fights Obesity, and aids the Digestive system.",
			place = "China and Korea",
			nut_cont = "Calcium, Potassium, Phosphours, Quercetin, Magnesium.",
			other_name = "Lagerstroemia",
			season = "Mid May and Early June", 
			soil_condi = "Plant grows efficently in wet, clay sand ", 
			other_use = "It is also used to make paste with flowers that can be applied externally to cuts and wounds. Root is astringent, detoxicant and diuretic. Decoction of the flowers is used in the treatment of colds. ", 
			scien_name = "Lagerstroemia", 
			charac = "These are best sown as soon as it is ripe. When they are large enough to handle, prick the seedlings out into individual pots and grow them on until large enough to plant out.Cuttings of half-ripe wood, 5 - 8cm with a heel. Fair to good percentage.Cuttings of mature wood.Root cuttings 4cm long. High percentage.",
			side_effects = "Reported side effects is pregnancy and breast-feeding: Not enough is known about the use of banaba during pregnancy and breast-feeding. Stay on the safe side and avoid use.")

obj21 = leaf(leaf_name = "Crepe myrtle",
			med_use = "It is used to regulate blood Pressure, fights Obesity and aids the Digestive system and used to cure Diabetes.",
			place = "China and Korea",
			nut_cont = "Calcium, Potassium, Phosphours, Quercetin, Magnesium.",
			other_name = "Crapemyrtle, Crape Myrtle, Crepe Myrtle, Crepeflower, Pride of India,  Queen Crape Myrtle",
			season = "All season", 
			soil_condi = "Plant grows efficiently in a sunny location. Soil need not be rich or amended; crepe myrtle trees are adaptable to most soils except those that are soggy. Sunlight and well-draining soil afford a wealth of summer blooms and help keep pests away.", 
			other_use = "It is also used to make paste with flowers that can be applied externally to cuts and wounds. Root is astringent, detoxicant and diuretic. Decoction of the flowers is used in the treatment of colds. ", 
			scien_name = "Lagerstroemia indica", 
			charac = "These are best sown as soon as it is ripe. When they are large enough to handle, prick the seedlings out into individual pots and grow them on until large enough to plant out.",
			side_effects = "Reported side effects is pregnancy and breast-feeding: Not enough is known about the use of banaba during pregnancy and breast-feeding. Stay on the safe side and avoid use.")

obj22 = leaf(leaf_name = "oleander",
			med_use = "It is used to treat Heart diseases, Asthma, Skin problems and Warts.",
			place = "East Coast of the US",
			nut_cont = "Oleander is no longer considered safe due to extreme toxicity. Extreme caution should be used because of its acute cardiotoxicity, hepatotoxicity, and nephrotoxicity.",
			other_name = "Adelfa, Baladre, Cascabela thevetia, Cerbera thevetia",
			season = "February to June", 
			soil_condi = "Plant grows efficently in poor soil, salt and spray,nutrient-rich, containing clay chalky, high pH levels and even severe pruning. As it can take the reflected heat from pavements, roads or walls as well as drought, it is popularly planted as the road dividers. However, oleanders cannot tolerate withstanding is too cold or freezing temperatures ", 
			other_use = "It is also used in literature, film, music and In painting", 
			scien_name = "Nerium oleander", 
			charac = "These are considered by many to be the most poisonous plant in the world. ... The plant grows as a dense shrub, and is typically 6 to 18 feet (1.8 to 5.4 meters) tall at maturity. It has thick, dark green leaves, and the flowers, which grow in clusters, can be yellow, red, pink or white.",
			side_effects = "Reported side effects is children: Oleander is LIKELY UNSAFE when taken by mouth in children. Taking the oleander leaf, oleander leaf tea, or oleander seeds has led to deadly poisonings.   Oleander can stimulate the heartbeat. Calcium might also affect the heart. Taking oleander along with calcium might cause the heart to be too stimulated. Do not take oleander along with calcium supplements.")

obj23 = leaf(leaf_name = "yew plum pine",
			med_use = "It is used to cure Blood disorders and Ringworm. ",
			place = "Southern Japan and Eastern China.",
			nut_cont = "Nitrogen, Phosphorus",
			other_name = "Japanese yew,Yew plum pine,Buddhist pine,Fern pine,Arhat pine,Yew podocarpus",
			season = "February to March", 
			soil_condi = "Plant grows efficently in well drained soil. The tree can handle moist soil but is likely to develop root rot in soggy conditions. It does well in sandy soil and coastal conditions, including salty sea spray.", 
			other_use = "It is also used for making furniture, utensils, paper, and farm implements.", 
			scien_name = "Podocarpus macrophyllus", 
			charac = "These are dense upright, large size evergreen shrub or small tree that grows about 20 m tall with 60 cm trunk diameter. The plant is found growing in forests, open thickets, and roadsides from near sea level to 1000 m. The plant can be grown in rich, slightly acidic, well-drained soils in full sun to part shade. It is tolerant of shade and intolerant of wet soils. The plant may develop chlorosis (yellowing of the leaves) in alkaline soils. The plant has gray or grayish brown bark",
			side_effects = "Reported side effects is it can cause severe stomach problems and can cause the heart rate to slow down or speed up dangerously. Signs of poisoning might include nausea, dry mouth, vomiting, stomach pain, dizziness, weakness, nervousness, heart problems, and many others. Death has occurred after taking 50-100 grams of yew needles")

obj24 = leaf(leaf_name = "Japanese Flowering Cherry",
			med_use = "It is used in the treatment of cancer",
			place = "Japan, China and Korea",
			nut_cont = "Protein",
			other_name = "Yamazakura, Japanese Flowering Cherry, Oriental Cherry",
			season = "September to March", 
			soil_condi = "Plant grows efficently in chalk,clay,loam,sand", 
			other_use = "It is also used in fishing as some tribes use fruit of Japanese cheesewood to attract and kill fish in the streams. This method facilitates collecting of fish from the water.", 
			scien_name = "Prunus serrulata", 
			charac = "These are a small deciduous tree that can reach 15-25 ft. ... Depending on the cultivar, it may feature an upright habit, a wide spreading habit with horizontal branching or a weeping habit.",
			side_effects = "Reported side effects are poisonous. However, the bean-like seeds are especially poisonous. Ingesting even two of them can cause serious poisoning in a child.")

obj25 = leaf(leaf_name = "Glossy Privet",
			med_use = "It is used to treat Diminished Eye Sight, Dizziness and to increase Immune function in Cancer patients",
			place = "North-East Europe and Great Britain",
			nut_cont = "Nitrogen, Phosphorus",
			other_name = "Chinese Privet Glossy Privet, Tree Privet.",
			season = "March to June", 
			soil_condi = "Plant grows efficently in adverse condition drought, heat, cold, many soil types and salt spray.", 
			other_use = "It is also used for promoting growth and darkening of hair, reducing facial dark spots, rapid heartbeat ", 
			scien_name = "Ligustrum lucidum", 
			charac = "These are an evergreen tree growing to 10 m (33 ft) tall and broad. The leaves are opposite, glossy dark green, 6–17 centimetres (2.4–6.7 in) long and 3–8 centimetres (1.2–3.1 in) broad. The flowers are similar to other privets, white or near white, borne in panicles, and have a strong fragrance, which some people find unpleasant",
			side_effects = "Reported side effects is  that those who have a sensitivity to ligustrum should avoid taking it in order to avoid complications from usage. Those who have allergies to plants such as olive, ash, and lilac should avoid taking ligustrum, as these plant species are of the same family and have similar characteristics, including allergic reactions.")


obj26 = leaf(leaf_name = "Chinese Toon",
			med_use = "It is used to lower blood sugar, help defend the body against oxygen loss  and help reduce fertility issues.",
			place = "Asia",
			nut_cont = "Ascorbic acid, Vitamin E",
			other_name = "Chinese mahogany, Chinese cedar, Chinese toon, beef and onion plant, or red toon",
			season = "February to March", 
			soil_condi = "Plant grows efficently in full sun but will tolerate some shade. Chinese toon prefers rich, moist, well-draining soil with a pH of 5.5-8.0. The optimal germination temperature for toona sinensis is 25 C°.", 
			other_use = "It is also used as a condiment to serve with plain rice porridge as breakfast and simple meals, or to enhance the flavour of a dish or soup.", 
			scien_name = "Toona sinensis", 
			charac = "These are crisp, crunchy, and distinctly aromatic, offering a floral, onion-like aroma when fresh. When cooked, they impart an earthy, pungent flavor that tastes like a combination of garlic, mustard greens, and fermented chives.",
			side_effects = "Reported side effects is toxic to animals")

obj27 = leaf(leaf_name = "Peach",
			med_use = "It is used to treat to treat gastric, stomach irritations and abdominal tenderness, irritation or congestion",
			place = "Kunlun Mountains",
			nut_cont = "Vitamin A, vitamin C, Protein",
			other_name = "Malum persicum,Persian apple,Persian plum",
			season = "July to September", 
			soil_condi = "Plant grows efficently in pH of the soil should be between 5.8 and 6.8. Acidic and saline soils are unfit for peach cultivation. The land with gentle slope is ideal for peach cultivation.", 
			other_use = "It is also used to add in green smoothies, oatmeal, brown rice porridge, quinoa, even salads, chia pudding, and more.", 
			scien_name = "Prunus persica", 
			charac = "These has yellow or whitish flesh, a delicate aroma, and a skin that is either velvety (peaches) or smooth (nectarines) in different cultivars. The flesh is very delicate and easily bruised in some cultivars, but is fairly firm in some commercial varieties, especially when green.",
			side_effects = "Reported side effects is the skin of peaches should be avoided, as the hair-like protrusions on the skin of peaches can cause allergies of the throat or otherwise aggravate the throat.")

obj28 = leaf(leaf_name = "Ford Woodlotus",
			med_use = "It helps to boost your heart function better, fights infections and can enliven your hair and skin with vitality.",
			place = "No data",
			nut_cont = "No data",
			other_name = "No data",
			season = "No data", 
			soil_condi = "No data", 
			other_use = "No data", 
			scien_name = "No data", 
			charac = "No data",
			side_effects = "No data")

obj29 = leaf(leaf_name = "Trident Maple",
			med_use = "It is incorporated in skincare products to prevent wrinkles",
			place = "Eastern China, Taiwan and Japan",
			nut_cont = "No nutritious content.",
			other_name = "Acer buergerianum,China maple",
			season = "December to January", 
			soil_condi = "Plant grows efficently in the Japanese akadama clay", 
			other_use = "It is also used in bonsai. Other uses can be as a street tree or a shade tree for smaller spaces", 
			scien_name = "Acer buergerianum", 
			charac = "These are thick-set trunk, and the upper back peels off easily to expose an under-bark that is pale orange in color.",
			side_effects = "Reported side effects are toxic to horses but nontoxic to dogs, cats and humans.")

obj30 = leaf(leaf_name = "Beales barberry",
			med_use = "It is used in traditional medicine for centuries to treat digestive issues, infections, and skin conditions.",
			place = "Europe",
			nut_cont = "Protein",
			other_name = "Mahonia bealei,Leatherleaf Mahonia",
			season = "All season", 
			soil_condi = "Plant grows efficently in light (sandy), medium (loamy) and heavy (clay) soils and can grow in heavy clay soil.", 
			other_use = "It is also used in cooking as it is nice when added to muesli or porridge. Unfortunately, there is relatively little flesh and a lot of seeds", 
			scien_name = "Mahonia bealei", 
			charac = "These are an evergreen Shrub growing to 2 m (6ft) by 2 m (6ft) at a slow rate. It is hardy to zone (UK) 6 and is not frost tender. It is in leaf all year, in flower from January to March, and the seeds ripen from April to May.",
			side_effects = "Reported side effects are the heart/blood vessel system (eg, low blood pressure, decreased heart rate) and decreased breathing may occur with high dosages.")


obj31 = leaf(leaf_name = "southern magnolia",
			med_use = " It is used to treat Malaria, Rheumatism and  Dropsy.",
			place = "South-East US and Atlantic ",
			nut_cont = "vitamin C, vitamin E",
			other_name = "Bull bay,Magnolia grandiflora,Him champa",
			season = "All season", 
			soil_condi = "Plant grows efficiently in moist, well-drained, acidic soils. It is tolerant of high moisture levels and can be planted in areas prone to wet/dry fluctuations in soil moisture.", 
			other_use = "It is also used to make furniture, pallets, and veneer.", 
			scien_name = "Magnolia grandiflora", 
			charac = "These are tall, rarely growing to 100 ft. They have a dense growth of smooth, leathery evergreen leaves that are alternate, 5-10 inches long, shiny on top and rusty below. Fragrant, creamy-white flowers, which discolor easily if bruised, appear on the ends of thick, tough stems all over the tree.",
			side_effects = "Reported side effects is taking magnolia flower bud by mouth is UNSAFE during pregnancy. There are reports that magnolia can cause the uterus to contract and that might cause a miscarriage. Not enough is known about the safety of using magnolia bark during pregnancy. Stay on the safe side and avoid use.")

obj32 = leaf(leaf_name = "Canadian poplar",
			med_use = "It is used in the treatment of Throats, Headaches, Sore Muscles and Joints.",
			place = "Canada",
			nut_cont = "Iron, Protein, Calcium, Potassium,Vitamin A",
			other_name = "Carolina poplar",
			season = "March to June", 
			soil_condi = "Plant grows efficiently in light (sandy), medium (loamy) and heavy (clay) soils and prefers well-drained soil. Suitable pH: acid, neutral and basic (alkaline) soils. It cannot grow in the shade. It prefers moist soil. The plant can tolerates strong winds but not maritime exposure.", 
			other_use = "It is also used in making the staves of barrels and woodenware, it turns well. It makes an excellent fuel. easily worked, rather woolly in texture, without smell or taste, of low flammability, not durable, very resistant to abrasion.", 
			scien_name = "Populus × canadensis", 
			charac = "These are simple, alternate, roundish and toothed. Bark of young trees is smooth, yellowish green, becoming grayish green to brownish and furrowed. Male and female flowers are clustered in drooping catkins on separate trees. Wind-pollinated flowers appear before leaves; seed matures as leaves develop.",
			side_effects = "Reported side effects is when applied to the skin. It may cause allergic skin reactions in some people.")

obj33 = leaf(leaf_name = "Chinese tulip tree",
			med_use = "It is use in the treatment of indigestion, dysentery, rheumatism, coughs, fevers, diarrhea, & inflammation.",
			place = "Eastern North America",
			nut_cont = "Vitamins,Minerals and Antioxidants",
			other_name = "Liriodendron chinense",
			season = "March to June", 
			soil_condi = "Plant grows efficiently in Clay, Loam, Sand and the soil must be moist but well-drained", 
			other_use = "It is also used for a variety of wood-based projects such as flooring, siding, furniture and fencing. The wood is generally light off-white to yellow-brown that darkens with age outdoors.", 
			scien_name = "Liriodendron chinense", 
			charac = "These are fast-growing, Liriodendron chinense (Chinese Tulip Tree) is an upright, spreading deciduous tree. In late spring to early summer, tulip-shaped, yellowish-green flowers, 1.5 in. long (4 cm), appear after the leaves on mature trees (at least 12-15 years old).",
			side_effects = "Reported side effects is toxicity in horse when a portion of the plant and/or the bulb is ingested.")

obj34 = leaf(leaf_name = "Tangerine",
			med_use = "It is used to treat Asthma, Indigestion, Clogged Arteries and used as a cancer prevention.",
			place = "Southeast Asia",
			nut_cont = "Rich Vitamin A, Vitamin C,Fiber.",
			other_name = "Citrus Reticulata, mandarin orange tree, mandarin, mandarin orange.",
			season = "December to March", 
			soil_condi = "Plant grows efficiently in wide variety of soils, but the trees do best when planted in fertile, well-drained soil. A mixture of manure, peat moss and rich compost is a suitable growing medium", 
			other_use = "It is also used to promotes Hair Growth & Delays Hair Greying.Vitamin A Helps To Moisturize The Sebum In The Scalp", 
			scien_name = "Citrus tangerina", 
			charac = "These are smaller than other orange trees. It bears slender twigs and glossy lance-shaped evergreen leaves. The white five-petalled flowers are fragrant. The fruit is slightly flattened at either end and has a loose reddish orange peel and easily separated segments",
			side_effects = "Reported side effects is also possible to consume too much vitamin C (more than 2,000 milligrams a day); an excess of this nutrient may lead to diarrhea, nausea, vomiting, heartburn, bloating or cramps, headaches and insomnia,")

obj35 = leaf(leaf_name = "Neem",
			med_use = "Neem leaf is used for leprosy, eye disorders, bloody nose, intestinal worms, stomach upset, fever, diabetes, gum disease (gingivitis), and liver problems. ",
			place = "South Asia",
			nut_cont = "Protein (7.1%), carbohydrates (22.9%), minerals, calcium, phosphorus, vitamin C, carotene ",
			other_name = "Azadirachta indica,nimtree,Indian lilac",
			season = "All season",
			soil_condi = "The Neem grows on almost all types of soils including clay, saline and alkaline soils, with pH up to 8.5, but does well on black cotton soil and deep, well-drained soil with good sub-soil water",
			other_use = "The antioxidants in neem are beneficial for reducing melanin production of your skin, which helps to even out your skin tone. It also reduces the dark spots, blemishes and any kind of redness on your skin.",
			scien_name = "Azadirachta indica ",
			charac = "Neem can reach 15–30 metres (49–98 feet) in height and have attractive rounded crowns and thick furrowed bark. The compound leaves have toothed leaflets and are typically evergreen but do drop during periods of extreme drought.",
			side_effects = "Pregnancy and breast-feeding: Neem oil and neem bark are LIKELY UNSAFE when taken by mouth during pregnancy. They can cause a miscarriage.")

obj36 = leaf(leaf_name = "Tulasi",
			med_use = "Tulsi can cure fever,used to treat skin problems like acne, blackheads and premature ageing and treat insect bites.",
			place = "Southeast Asia",
			nut_cont = "Tulsi leaves are rich in vitamins A, C and K and minerals like calcium, magnesium, phosphorus, iron and potassium. It also has a good amount of protein and fibre.",
			other_name = "Tulsi ,Ocimum tenuiflorum,Holy basil",
			season = "April to June",
			soil_condi = "Tulsi requires aerated, porous, well drained soil with added organic manure. Sticky, clay like soil is not good for plants roots.",
			other_use = "Camphene, cineole, and eugenol present in Tulsi helps to reduce cold and congestion in the chest. Juice of Tulsi leaves mixed with honey and ginger is effective in bronchitis, asthma, influenza, cough and cold.",
			scien_name = "Ocimum tenuiflorum",
			charac = "Tulsi is an upright bushy shrub that grows up to 18 inches. It's hairy stems sprout oval leaves with serrated edges, and depending on the variety, range in color from light green to dark purple. The tulsi plant blooms erect purple or reddish flowers and produces tiny rust-colored fruit.",
			side_effects = "But larger medicinal amounts are POSSIBLY UNSAFE. Basil contains a chemical, estragole, which has caused liver cancer in laboratory mice. Bleeding disorders: Basil oils and extracts might slow blood clotting and increase the risk of bleeding in people with bleeding disorders.")

obj37 = leaf(leaf_name = "Aloevera",
			med_use = "Aloevera gel typically is used to make topical medications for skin conditions, such as burns, wounds, frostbite, rashes, psoriasis, cold sores, or dry skin.",
			place = "North Africa, Southern Europe,Canary Islands and South Asia",
			nut_cont = "Aloe vera contains 75 potentially active constituents: vitamins, enzymes, minerals, sugars, lignin, saponins, salicylic acids and amino acids.",
			other_name = "Chinese Aloe, Indian Aloe, True Aloe, Barbados Aloe, Burn Aloe, First Aid Plant.",
			season = "February to June",
			soil_condi = "Grow best in dry conditions. When growing aloe vera plants, plant them in a cactus potting soil mix or a regular pot. Also, make sure that the pot has plenty of drainage holes. Aloe vera plants cannot tolerate standing water.",
			other_use = "Aloe vera has been one of the most important plants used in folk medicine. It is traditionally used for wound healing, to relieve itching and swelling, as well as for its anti-inflammatory properties",
			scien_name = "Aloe barbadensis miller.",
			charac = "Aloe vera is a stemless or very short-stemmed plant growing to 60–100 cm (24–39 in) tall, spreading by offsets. The leaves are thick and fleshy, green to grey-green, with some varieties showing white flecks on their upper and lower stem surfaces. The margin of the leaf is serrated and has small white teeth.",
			side_effects = "Aloe vera ingested in high amounts may induce side effects, such as abdominal pain, diarrhea or hepatitis.")

obj38 = leaf(leaf_name = "Ashwagandha",
			med_use = "Ashwagandha is a medicinal herb that may offer several health benefits, such as improved blood sugar, inflammation, mood, memory, stress and anxiety, as well as a boost in muscle strength and fertility. ",
			place = "North-western and central parts of India",
			nut_cont = "Magnesium and vitamin B6.",
			other_name = "Indian ginseng, poison gooseberry, or winter cherry,",
			season = "January to March",
			soil_condi = "The soil should be loose, deep and well-drained. Ashwagandha grows well in sandy loam or light red soils having pH 7.5-8.0. Black or heavy soils having good drainage are also suitable for ashwagandha cultivation",
			other_use = "Ashwagandha do really helps in gaining height,as it helps in gaining muscle and bone mass meaning increase in all three dimensions.",
			scien_name = "Withania somnifera",
			charac = "It is a fairly small shrub with small pale green flowers, simple leaves and red berries. It has a tuberous root, carrot or ginger shaped. It also has a distinct smell, described as horse-like, which is where it gets its name, ashwagandha; Ashwa is Sanskrit for horse and gandha for smell.",
			side_effects = "when taken for up to 3 months. The long-term safety of ashwagandha is not known. Large doses of ashwagandha might cause stomach upset, diarrhea, and vomiting. Rarely, liver problems might occur.")

session.add_all([obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9, obj10, obj11, obj12, obj13, obj14, obj15, obj16, 
obj17, obj18, obj19, obj20, obj21, obj22, obj23, obj24, obj25, obj26, obj27, obj28, obj29, obj30, obj31, obj32, obj33, obj34, obj35, obj36, obj37, obj38])

session.commit()


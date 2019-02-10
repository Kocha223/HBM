# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define a = Character("Alex")

define m = Character ("Myra")

define t = Character ("Taisa")

define n = Character ("Matthew")

# The game starts here.

label start:

    scene black

    "Crewman" "\"Doctor? Doctor are you awake?\""

    "I blink away the sleep from my bleary eyes. The ship jostles again, and for a moment I freeze as my hammock lurches."

    "The weightlessness lasts only for a moment before the ship crests the wave and everything comes crashing down."

    a "\"Oh goddamnit...\""

    "My hammock overturns, and I tumble to the wet planks below. An instant later, my instruments fall from their shelves and scatter across the floor."

    "Crewman" "\"Doctor, are you alright? What's going on in there?\""

    a "\"I'm fine! Quite fine! Just give me a moment.\""

    "I hastily throw on my coat and answer the door."

    "Crewman" "\"Thank the Dragon, Doctor! Hurry quick, we need you atop!\""

    a "\"Atop in this weather? Not to man the sails I hope!\""

    "Crewman"  "\"No sir, of course not! It's Allen, he fell from the yards! He's not breathing!\""

    "I can hear the fear in his voice. Without hesitation, I rush up the hatch-steps against a tide of seawater. The rain hits me the moment I'm on deck. I turn away, shielding my eyes in vain against the near-horizontal torrent."

    show ship stormy with fade

    "The ship lurches beneath me, and I grab hold of the railing as men stumble across the deck."

    "The water rises and falls, churning like a boiling pot. How did we ever get into this mess?"

    a "\"Where is he?\""

    "I shout to be heard, and the crewman leads me over to a crowd of men by the {i}Raider's{/i} mainmast."

    a "\"Move aside, you men!\""

    "They scatter as I bark at them, and I kneel next to the body on the deck. The boy is dead, poor soul, I don’t need to check a pulse to know it. But I take it anyway."

    "???"  "\"Doctor Wray!\""

    "The voice is almost inaudible beneath the howling wind. Captain Trevors stands upon the quarterdeck, struggling against the wheel. I strain to hear his shout."

    "Trevors"  "\"Get you a lifeline, Doctor! One wave and you're done for!\""

    "I realize the truth of his words just a moment too late."

    "Lightning strikes the mainmast, and it tears free with a hideous crack. The mast falls into the violent sea to windward, dragging its rigging behind like an anchor chain."

    "The boat groans, slows, and then begins to turn into the wind."

    "Trevors shouts, near panic, and the sailors set at the thick ropes with axes and knives, desperate to cut loose the dead weight before we broach."

    "But before they can free the ship, another wave strikes the {i}Raider{/i}, sweeping over the deck without any resistance."

    "I let out a shrill yell as the wave drags me along with it. I grope for a line, the taffrail, anything! But it's no use. The wave carries me bodily over the side, into the dark waters below."

    scene black with fade

    "Waves. The sea's beating heart."

    "I can't be dead yet. Father always said there's no water in hell."

    show beach with fade

    "Wreckage litters the surf. Fifty or so yards out, a the {i}Raider’s{/i} battered topmast protrudes from the water like a grave marker."

    "I groan and struggle to stand. The moment I think I'm steady, my right ankle gives way, and I fall to my knees in the hot sand."

    "I blink as spots fill my vision, and my throat tightens with thirst. My voice is so hoarse it's almost unrecognizable."

    a "\"Ugh. Alrich's blood, where am I?\""

    "The jungle ahead is an impenetrable wall of foliage. It stretches down the coast in either direction, a distance so great that the green melds with the horizon’s blue.center."

    "This must be one of the islands off the Tetran coast. The Lorcan mariners call them the Stripes. So the stories go, the islands are crawling with monsterfolk."

    "Damn fine luck. I must be a hundred leagues from Tetra Magna. I may as well be on the shores of Arche Draconia."

    "On the other hand, the storm didn't take my necklace or bag. I suppose fate has a way of evening things out."  

    "I wrap my hand around the votive necklace, marked with the emblem of Lord Alrich. I'm usually not one for religion, but a prayer every now and then never hurt."

    "Especially this far from home."

    "I try to recall what I was told about these islands. Other than the human settlements of Port Harken and Free Harbor, the islands were entirely populated by monsters."

    "And not monsterfolk like those back home in Cassia, who've lived and intermarried with humans for centuries." 

    "The Tetran continent was different. Stories abound of sailors stranded, taken in by the locals, and {i}used{/i}."

    "The stories were always meant as a warning, but it didn't sound like much of a punishment to me." 

    "How did Father put it? Drowning in pussy wasn't far off from drowning in gold. You'll die all the same, but at least you're grinning start to... finish."

    "I grit my teeth as I drag my weary form through the brush. The thirst is almost unbearable. Every shake of my head sends stars dancing across my vision."

    "Ahead, I hear the trickle of running water. The faint noise echoes in my head as my body screams at me. I scramble onward in a frenzy. I burst through a wall of foliage and collapse gasping on a bed of soft, damp grass."

    show lagoon with fade

    "I race to the lagoon's edge. The cold water is like a razor against my parched throat, but I drink and drink until the urge to breath overwhelms my thirst."

    "Whatever god is watching over me, I owe it. Lord Alrich, if it's you, I swear I'll go to a service once this year. Maybe twice if it's convenient."

    "I hear a splash, and look up in search of the source of the sound."

    #CG shot with panning

    window hide

    show lagooncg1:
        xpos 0 ypos -770 zoom 1.25
        linear 3.0 xpos 0 ypos 0 zoom 1.25
    with fade

    pause 5

    show lagooncg1:
        xpos -3750 ypos -1500 zoom 2
        linear 6.0 xpos -3750 ypos -300 zoom 2
    with fade

    pause 8

    "My gaze trails up their nude forms, pausing upon the spots dotting their thighs and shoulders, and again on their rounded, feline ears. Monsterfolk. Jaguars to be precise."

    show lagooncg1:
        xalign 1.0 yalign 1 zoom 0.65
    with dissolve

    "The two glance at each other, then back at me, their tails swishing curiously behind them. The first, a lithe girl with a fringe of sunkissed hair and sharp features, gives me a contemptuous sneer."

    "The other is almost her opposite. Her full body oozes sensuality. My eyes are drawn again and again to her thick, welcoming thighs."

    "She smiles at me, the light catching on her sharp teeth."

    "I swallow heavily as the short-haired felid slips into the lagoon and begins to wade towards me."

    "Do I run? Panic turns my veins to ice. They'll catch me. Even uninjured, I'll never manage to escape. Bloody and barefoot as I am, it'd be a joke to even try."

    "But beyond that, perhaps I shouldn't run. These girls may be my best chance at surviving this nightmare."

    "I scramble to my feet and smile as the curvier of the two turns to the other."

    scene lagoon
    show myra naked neutral
    with dissolve

    "Jaguar" "\"Taisa! Taisa! A human! I can’t believe it!\""

    show myra naked neutral:
        xalign 0.80
        yalign 1.0

    with move

    show taisa nude scowl
    with dissolve

    t "\"What are you getting so excited about, Myra? You remember what mother said.\""

    "Her voice is as cold as her glare, but somehow I get the feeling the anger isn’t directed at me. Myra bounces on the balls of her feet and makes a petulant whine."

    show myra naked smug:
        xalign 0.80
        yalign 1.0

    with dissolve

    m "\"But we'll never know for sure if we leave him here! Come on, Taisa, look at him! Isn't he cute?\""

    show myra naked blush:
        xalign 0.80
        yalign 1.0

    with dissolve

    show taisa nude pout
    with dissolve

    "She licks her lips, and I give a nervous smile in reply. Looks like the stories were true. I'm still not sure if that's a good thing or a bad thing. I guess it's now or never."

    "I..."

    menu run_or_talk:

        "Just run":
            jump running_away

        "Try to talk my way out of this":
            jump smooth_talker

    label running_away:

        $ running_away = True

        "There's no way I'm taking any chances. I have to get out of here, and fast."

        "I spin on my heel and take off running. My legs scream out, burning with the sudden effort as I scramble back towards the treeline."

        show myra naked pout:
            xalign 0.80
            yalign 1.0
        with dissolve

        m "\"Hey!  Where do you think you're going? Taisa, stop him or something!\""

        show taisa nude scowl
        with dissolve

        t "\"Stop him yourself! You're the one who wanted to play with him in the first place.\""

        "Argue away, you two. Gives me more time to get away."

        show myra naked pout at center
        with move

        show taisa nude shocked at left
        with move

        show myra naked smug

        m "\"Fine, fine. You always make me do all the work.\""


        "I'm just feet from the treeline when I hear the patter of bare feet on wet stone and a rush of air. The hairs on the back of my neck stand on end, and I instinctively dodge to avoid Myra's hand."

        show myra naked smug:
            parallel:
                ease .25 zoom 2.0 
            parallel:
                linear 0.25 xalign 0.75 yalign 0.25
    

        a "\"Ah-\""

        "I duck just as her hand sweeps for my throat, but my feet slip on the uneven ground."

        "I topple backward, bowling over Myra and sending us both tumbling to the damp grass. I struggle to stand, but Myra pulls me back into her chest, one arm locked around my throat."

        m "\"Gotcha! I'm not letting you go this time!"

        show taisa nude scowl:
            ease 0.25 xalign 0.20

        t "\"Myra, you gotta be careful! Don't kill him!"

        "I kick for purchase on the grass, but Myra snakes her legs around mine and tightens her grip around my throat.  Darkness closes in on my vision as I fight for breath.  How the hell is she so strong?"

        show myra naked excited:
            zoom 2.0
            xalign 0.75 yalign .25
        with dissolve

        m "\"Hey, hey!  No need to fight so much!  I'm not that scary!"

        show myra naked pout:
            zoom 2.0
            xalign 0.75 yalign .25
        with dissolve

        m "\"Am I?\""

        "Terrifying actually, but I don't have the breath to tell her."

        m "\"What's your name?\""

        "I cough in reply, and in the corner of my hazy vision I see Taisa come up to our side.  She sighs and shakes her head."

        show taisa nude pout:
            ease 0.25 xalign 0.15

        t "\"Myra, I think you're killing him.\""

        show myra naked lewd:
            zoom 2.0
            xalign 0.75 yalign .25
        with dissolve

        "Myra lets out an embarrassed squeak and her grip loosens.  I gasp, choking for breath, then immediately I try to break free.  But her grip barely gives at all, and I'm in no shape to fight back."

        m "\"There we go!  What was your name again?\""

        #smalltext

        a "\"{size=-10}Alex...{/size}\""

        m "\"What kind of name is that?\""

        show taisa nude pout:
            ease 0.25 xalign 0.20

        t "\"A human name! What kind of name do you think?\""

        show taisa nude extra blush:
            ease 0.25 xalign 0.15

        t "\"Hey! Watch where you're letting him touch you!"

        show myra naked blush:
            zoom 2.0
            xalign 0.75 yalign .25
        with dissolve

        m "\"It's fine! It's fine!\""

        "I cough as Myra's grip loosens and she gets out from behind me.  With an almost casual air, she hefts me up to my feet."

        m "\"Shhh, everything will be just fine.  We'll get you to the village safe and sound.\""

        "Her words come muffled, as though she were speaking underwater.  The sudden jerk to my feet sends the blood rushing from my head, and all the hunger and fatigue wash over me at once."

        t "Hey, there he goes again! Unbelievable..."

        "I fall face first into Myra's breasts, her soft skin and the encroaching darkness all but blotting out Taisa's protests.  Myra holds me as my legs give out, pressing my face into her warm cleavage."

        "Well, there are worse ways to die."

        jump flashback_lorca

    label smooth_talker:

        #edit this.

        a "\"What a relief, I didn't think I'd find anyone out here. I'm shipwrecked, and I could use your help.\""

        show myra naked neutral:
            xalign 0.80
            yalign 1.0
        with dissolve

        m "\"shipwrecked? You came from across the sea?\""

        a "\"From Lorca, if that means anything.\""

        show taisa nude serious
        with dissolve

        "By Myra's blank expression, I'll have to assume it doesn't."

        a "\"I'm not sure if the ship survived the storm or if it went straight to the bottom of the sea, but I managed to cling onto a bit of wood and wash ashore.\""

        "Another rush of hunger and fatigue hits me.  Now that I've found someone to help me out, my body is starting to give up."

        show myra naked smug:
            xalign 0.80
            yalign 1.0
        with dissolve

        m "\"Taisa, we should take him back to the village.  I don't care what mom says, he needs our help!\""

        a "\"I need to get to Free Harbor as soon as possible. I appreciate any help you can...\""

        "My voice trails off as Taisa stops just in front of me, a hand on her hip. Now that she’s right in front of me, I’m stunned to silence. I follow a bead of water as it trails down her slender side, past her bared entrance, then down her muscular thigh."

        show myra naked blush:
            xalign 0.80
            yalign 1.0
        with dissolve

        m "\"Taisa, he's staring~\""

        show taisa nude extra blush
        with dissolve

        "I smile as a blush crosses Taisa's face. Even through the hunger and exhaustion, a little voice whispers in the back of my mind."

        "Who knew that 'drowning in pussy' would end up being a pun?"

        show taisa nude scowl
        with dissolve

        t "\"See something you like?\""

        "Taisa's renewed frown takes the wind from my sails, and I backpedal as best a man sporting a growing erection is able."

        a "\"W-wait, I'm not-\""

        "I slip on the wet stone and tumble backward, wheeling my arms in a vain effort to catch myself.  My head strikes the rock and I blink as stars flash before my eyes."

        show taisa nude shocked
        with dissolve

        "Myra shouts, but her words come as though I'm submerged. Myra couches at my side and lifts me onto her thighs as she cradles my face. Taisa stands astride me, looking down with a mixture of guilt and concern on her face."

        "Pressed against Myra’s bosom and with a clear view of Taisa’s nude figure, I can’t help but smile as the darkness closes in."

        "Well, there are worse ways to die."

        jump flashback_lorca

    scene

    scene

    label flashback_lorca:

    scene black
    with fade

    "The laughter of friends, the warm aroma of pipesmoke and fine liquor."

    show flashback smile
    with fade

    "I turn away as a chilly night breeze rushes through the bar, as a gang of new arrivals pile into the Jewel, my favorite watering hole."

    "The two girls at my side shriek and laugh, pressing themselves against me until the slamming door cuts off the flow of air."

    a "\"And that dears, is what the wine is for.\""

    "Helena, all doe eyes and rosy cheeks, squeezes my arm between her breasts and whimpers."

    "Helena" "\"Alex!  Can't we go over by the fire?\""

    "I shake my head and pour three fresh glasses, finishing off our second bottle of the evening."

    a "\"No chance dear.  This is my lucky table. The master always has it ready for me.\""

    "A boldfaced lie. I'm not near so well-liked by the owner to have my own table. Well, maybe if I paid off my tab from last year, but as is, I'm lucky to be served at all."

    "Rather, if we sat at the table by the hearth the window would look out over the river, and the pyres on the far side. Even at night, the fires burned outside the Archdeacon's hospital, quarantined these past seven months."

    "My colleagues at the medical institute, the living ones at least, say the toll will reach a thousand a day before long."

    "Maxine" "\"Alex, when are you going to take us to the opera? You promised!\""

    "Maxine tugs on my neckcloth, wrenching my attention back to my two companions."

    "Helena" "\"You did! You did!\""

    a "\"Oh Lord! Anything but the opera!\""

    "Time to put that university education to work and figure out how to talk them into my bed intead of the goddamn theatre."

    "Maxine and Helena press in on both sides, and for a moment it looks like I'm cooked. Then I catch a familiar shade of blue at the far end of the room. I raise my glass and shout out."

    a "\"Brother!\""

    show flashback matthew standing
    with fade

    "Matthew Nelson marches towards me, his pale face grim. Dressed in the uniform of a Lorcan officer, with a Grenadier's bearskin slung over one arm, his imposing figure parts the crowd around him."

    "Thank Alrich, I'm saved! He can pay my tab {i}and{/i} get me out of this bind."

    n "\"Alex, I thought I'd find you here.\""

    "His gaze passes from me to Helena, then to Maxine, then back to me. His disapproval grows."

    a "\"And now that you're here, you can join us for a drink! Come, come!\""

    n "\"You know I can't drink on duty.\""

    "Helena presses herself against me and casts a furtive glance at Matthew."

    "Helena" "\"Alex, dear? Who is he? Introduce us!\""

    "I sigh, nodding."

    a "\"Helena, Maxine, let me introduce my brother, Captain Matthew Nelson, of the 3rd Lorcan Grenadiers.\""

    "Both women let out a high-pitched \"ahh~\" and lean towards my brother as he pulls out a chair and sits across from us."

    show flashback matthew sitting
    with fade

    "Helena" "\"I hope you've given those Vitrian fiends a good thrashing!\""

    "Matthew's frown deepens in time with my grin."

    a "\"Oh, you can be sure of that. He won the Red Lion at the Battle of Hamon's Crossing, and was aboard the {i}Majestic{/i} when it took the {i}Leander{/i} and the {i}Bonaventure{/i}.\""

    "Helena squeals in delight, and for a moment it looks as though Matthew is about to strangle me."

    "Helena" "\"Oh, how thrilling! I'm so pleased to meet you! We're honored!\""

    "Helena" "\"But, Alex dear. You said his name was \"Nelson\"?\""

    a "\"I told you didn't I? Matthew's father adopted me after my parents died. I just couldn't give up my father's name.\""

    "Maxine" "\"Are you on leave?\""

    n "\"Business.\""

    "A chill passes down my spine."

    a "\"Last I heard you were stationed at Fort Acheron.  Why would they recall you?\""

    n "The General Staff has good reason to want me back in Lorca."

    n "\"For that matter, what are you doing here, Alex? Father would be disappointed to learn you've been squandering your pay here. Shouldn't you be at the College?\""

    a "\"And proofread another one of the headmaster's submissions? I think not. The man has it out for me. I hardly have a chance to work on the Plague, and when I do, it's in a morgue.  I haven't seen one live patient since graduation! What else am I to do but drink?\""

    "I frown and look away, too embarrassed to meet my brother's stoic gaze."

    show flashback matthew arm
    with fade

    n "\"With the plague as bad as it is, I’m surprised this place is even open.  Look at you, reveling while the world burns.\""

    a "\"I hope you didn't come here to lecture me, brother.\""

    n "\"No I-\""

    show flashback thugs 
    with fade

    "Matthew pauses as a shadow falls across him and turns to look over his shoulder at the four burly, ill-tempered men that had so suddenly appeared from the crowd."

    show flashback exit
    with fade

    "Helena and Martia take their leave- obviously put out of place by our tense conversation. The pair vanishe in a swish of skirts and a torrent of excuses, leaving Matthew and me alone with our new, far less appealing, guests."

    "Shabbily-dressed and bearing truncheons on their belts, the men are hardly bear the image of the Jewel's usual clientele. Some of the other patrons stare at our silent confrontation, and all around, the various conversations lull."

    show flashback matthew mad
    with fade

    n "\"Sod off, will you? I have business with my brother.\""

    "Thug #1" "\"Aye, as do we.\""

    "The man shifts his leery gaze to me."

    "Thug #1" "\"Alexander Wray.\""

    a "\"Doctor.\""

    "Thug #1" "\"Doctor Wray then, if it please you. You owe quite a penny and we've been hired to collect.\""

    "Matthew looks up at the man in disbelief, then turns his reproach fully onto me."
    n "\"How much?\""

    "I shrink back as he growls at me. There's no way I can answer that!"

    n "\"Alex!\""

    "Thug #1"  "\"I believe it’s twelve thousand, seven hundred, and forty-three Lorcan Crowns. Plus interest o'course.\""

    "Thug #2"  "\"Compounded daily.\""

    "Thug #1" "\"Daily, just so.\""

    "I lick my suddenly dry lips and smile nervously."

    a "\"Surely your patron has proposed terms?\""

    "Thug #1" "\"He's got terms for ya', pay up, or you'll be in a debtor's prison before the end of the week.\""

    a "\"I-\""

    n "\"Shut up, Alex.\""

    "He turns to the men."

    "Matthew stands and wrenches me to my feet before fixing the collector with a withering glare."

    n "\"The Lorcan army does not appreciate the civil service meddling in its affairs. Good day sir.\""

    "But the collectors don't budge, and soon another group shoves their way through the gathering crowd. Now seven in all, the men hem us in against the booth. His confidence renewed by the arrival of his friends, the thug grins and pats his truncheon."

    "Thug #1"  "\"Come on, boss. Let's get a move on.\""

    n "\"Run.\""

    a "\"I'm sorry, what?\""

    n "\"Run, you idiot!\""

    show flashback fight
    with dissolve

    "Before the bailiffs or I understand what's going on, Matthew spins about and decks the first thug with a monstrous blow. The others scatter as Matthew lays into them, roaring."

    "In my case at least, discretion is the better part of valor, and I'm not one to disregard my brother's carefully considered advice."

    a "I'll leave the riff-raff to you, brother!"

    "I leap over the booth and make for the door.  Behind me, Matthew's laughter fills the room, almost loud enough to drown out the groans of his victims."

    "I burst through the door and rush down the city street, dodging through alleys and storefronts as I make my bid for safety."

    scene alleyway
    with fade

    "I pause for a rest in the shadow of an alleyway.  Mere minutes later, Matthew joins me."

    show matthew serious
    with dissolve

    "His face is only a slight red, beaded with the faintest sheen of sweat."

    a "\"Hah… that was… quite the thrill… eh Matthew?\""

    n "\"If there’s anyone I don’t mind toppling, it’s a debt collector. But those women, I thought you were seeing that Eliza girl?\""

    a "\"No, we parted ways. I’ve come to realize that screwing married women is an exercise in marginal utility.\""

    n "\"But really, Alex.  You’re lucky I was there. Those men would have given you something to complain about.\""

    a "\"They still might. It’s not like I can leave the city while the Headmaster still has work for me.\""

    n "\"I've seen to that.\""

    "He reaches into his jacket and removes an envelope, crumpled almost beyond recognition yet still bearing the seal of the Lorcan High Council. I cock my head in confusion."

    n "\"You should be grateful. I did solve your little debt problem, but it involves conscripting you into the Lorcan Army.  Congratulations, you're now a 2nd Lieutenant.\""

    a "\"You're joking?  What in frigid hell could the General Staff want with an underachieving doctor?"

    "I peel open the envelope and let the single sheet of parchment fall into my hand. Mouthing the words in a hasty mumble, I scan the contents."

    "{i}Dear Doctor Wray, congratulations on your appointment to 2nd Lieutenant, and thank you for your service to the Crown and the Coalition. You are hereby appointed to the Sloop-of-War Sunset Raider, departing immediately for the Tetran continent.{i}"

    "{i}There, in an effort to discover a cure for the Crying Plague, you are to search out the plant known as the Pale Bloom.{i}"

    a "\"Are you fucking kidding me, Matthew?\""

    n "\"They're quite serious, I assure you.\""

    "This is unbelievable. Conscription is one thing, but this is something else. I'm not saying one thing or another until he can answer a few of my questions."

    menu flashback_questions:

        "\"The Pale Bloom is a myth.\"":
            jump palebloom_explanation

        "\"Is this really worth the trouble?\"":
            jump last_hope

        "\"Does the General Staff really believe I'm the right man for the job?\"":
            jump lazy_doctor

    label palebloom_explanation:
        $ palebloom_explanation = True

        a "\"The Pale Bloom is a myth, Matthew, as is the exilir it creates.  This was first year stuff at the medical institute.\""

        n "\"You're wrong, and there's proof.\""

        "I raise an eyebrow."

        a "\"Show me then.\""

        n "\"Not that kind of proof, you dumb bastard.  One of our agents in Tetra Magna has sent over a few fossilized samples.  She at least, believes the rumors.\""

        a "\"So you have the word of one doctor to go on?\""

        n "\"Would you believe the Vitrians?  Our spies have noticed a twofold increase in their shipments to Tetra.\""

        n "\"The plague hit them harder than it did us.  If they could find a cure, their advantage would be absolute.\""

        jump flashback_questions

    label last_hope:
        $ last_hope = True

        a "\"is this business really worth the trouble, Matthew?\""

        n "\"The General Staff has devoted substantial resources to the operation, yes.\""

        a "\"That's not really what I mean.  The war is still carrying on in full force isn't it?  Wouldn't these funds be better spent on casting cannon and shot?\""

        n "\"You didn't hear this from me, Alex.  The General Staff has decreed that another levy is due at the year's end.\""

        a "\"What?\""

        n "\"Between the plague and the war, we're running out of men.  A shot in the dark or not, the Staff intends to carry this mission to the end.\""

        jump flashback_questions

    label lazy_doctor:
        $ lazy_doctor = True

        a "\"This is ridiculous.  I'm the man they want to send?\""

        a "\"And I’m the man they want to send?\""

        n "\"You’re the son of Argus Nelson, the greatest explorer of our age.\""

        a "\"And so are you.\""

        n "\"I never took to his lessons like you did.\""

        n "\"I’m not sure anyone else could survive in the Tetran wilds, and even if they could, would they have the medical knowledge to find what they’re looking for?\""

        "He’s right, of course. There are better doctors, but not one I’d trust outside a lab. I could survive, hell, {i}thrive{i} in Tetra."

        "And I've always heard such good things about Tetran women. After years of women demanding to be called \"My Lady\" in the bedroom, I could use a good romp in the wilds."

        jump treatment

    scene

    scene

    label treatment:

        #figure out what to do here

    "Too much light."

    "I blink and turn my head to escape the brilliant beam of morning sunlight."

    "The world is blurry, sounds muffled."

    "White crowds at the edge of my vision, pulsing in time with the beating of my heart."

    #Myra sprite blurry

    "Wait. Don't go."

    #Taisa sprite and Myra

    "Voices."

    #sprites close in

    "A wet cloth on my forehead."

    "Are they helping me?"

    "A face leans in close, lips curled in a smile."

    "Myra?"

    scene

    scene

    label Myra_handjob:

    "I wake to a hand gently shaking me."

    m "\"Hey, Alex.  You can't still be sleeping!\""

    "With great effort, I manage to open my eyes just a hair. Bathed in the deep light of the late afternoon, the room swims before my eyes."

    m "\"Hey, come on!  I know you’re awake.\""

    "I shiver as her whiskers tickle my face. I feel her hot breath on my ear."

    m "\"Do you need a kiss to wake you up? Or maybe, something else?\""

    "Her hand drifts down my chest and slips beneath the sheets."

    m "\"Oh? Look at you! I’ve barely touched you, and you’re already like this?\""

    "Spurred on by her scandalous whisper, my half-hard cock practically leaps into her waiting hand."

    "Myra giggles, and wraps her cool fingers around the length of my shaft."

    m "\"How long will you be able to last?\""

    a "\”Ah-\""

    "I groan as she gives my cock a slow, fulsome stroke.  Myra giggles at my reaction and gives me a quick squeeze.  I buck my hips out of reflex, and she lets out a surprised gasp."

    a "\”Hey, wait a-\""

    m "\”Shh, you’re supposed to be asleep.\""

    "I let out a ragged breath as she draws her hand up and down again.  I push up against her agonizingly slow strokes, my cock throbbing in her firm grip."

    "I try to sit up, but Myra forces me back down into the mattress, straddling my legs.  Her nails dig playfully into my chest.  Then she traces her hand down my body to join the other around my length."

    m "\”It feels good, right?  Right?\""

    "Myra coos as she takes me in both hands, then teases the tip with a fingertip.  I bite my lip and struggle against her grip, but her firm thighs have me locked in place."

    m "\”Oho?  What do we have here?\""

    "Myra’s eyes widen as a bead of precum bubbles up between her fingers.  She hums to herself as she plays the glistening fluid between her fingertips, then gives me a sideways glance brimming with lust."

    m "\”Wow, look at how excited you are!\""

    a "\”Quit messing around!\""

    m "\”Oh? You don’t like being teased?  All those months on that ship must have been unbearable.\""

    "She leans over-top me, her full breasts rubbing up the length of my body as she lowers herself to whisper in my ear."

    m "\”Don’t worry one bit.  I’ll make up for every wasted minute.\""

    "Myra returns to her position atop my knees and starts to stroke me again.  Wetting her palms with my dripping precum, she steadily pumps my shaft.  I arch my back, pressing myself into the warmth of the mattress as something begins to rise up within me."

    a "\”Myra, I’m-\""

    "An ecstatic grin crosses Myra’s face seconds before I cum.  I buck my hips into her waiting hands, spraying four thick ropes of semen across her full chest."

    m "\”Aha~\""

    "Myra giggles, and traces a finger down the curve of her breasts, gathering a dollop of my cum on her finger.  With a devilish grin, she brings the finger to her mouth and licks it clean."

    a "\"Lord, I needed that.\""

    "I move to sit up, but Myra has hardly shifted, her hand still tight around the base of my cock."

    a "\"Myra?\""

    m "\"What? Don’t tell me you’re satisfied with just that?\""

    a "\"Well-\""

    "Myra gives my cock a single stroke, sending a shiver of pleasure down my spine. If anything the sensations are heightened now that she’s already brought me to my peak.\""

    m "\"Don’t be bashful! This part of you still wants to play!\""

    "Myra delights in her messy work. She lowers a hand to cup my balls, tugging gently in time with her now more-rapid strokes. Her breath comes in heavy pants, just shy of outright moaning."

    #check that this works with the audio

    m "\"Hehe, you look like you're having fun! Don’t tell me you’re about to cum again already!\""

    "With both hands, Myra’s expert motions form an uninterrupted chain of pleasure around me.  The slick sound of her fingers flowing around me is far too much for me to bear."

    "I clench my eyes shut as I cum again, the second time in as many minutes.  Stars flash before my eyelids, and I press myself back into the sheets."

    a "\"That felt-\""

    m "\"Must have been pretty good, right?  That was almost more than the first time!\""

    "I blink away the spots in my vision to catch a glimpse of Myra’s cum-soaked form.  The sight of her body marked with my seed is enough to get another twitch out of my cock, and Myra looks down with a surprised, but undeniably pleased expression."

    m "\"I thought I was the monster here. Let’s see if I can get one more shot out of you~\""

    "Myra’s shapely ass sways back and forth in time with the flick of her tail. Her skirt hangs dangerously off to one side, just inches away from baring everything."

    "Pride wells within me as a trail of translucent arousal drips down her thigh to join the damp spot on the bedding beneath her. Myra stifles a moan and presses her legs together in a vain attempt to stem the flow."

    "When they part again, her full thighs are slick and glistening."

    a "\"Myra...\""

    "I whisper her name as her pace quickens. Her smoky eyes watch my every shift as she brings me closer and closer to my limit.\""

    m "\"You're close again, aren't you?\""

    "I manage a nod, and she moans in reply."

    m "\"I’m not gonna go easy on you this time.  I want you to earn this one.\""

    "Her pace, which had been quickening steadily, suddenly drops off, and I feel a sudden longing rush down my spine. I buck my hips up at her, but Myra just tightens her thighs around me, locking me in place.\""

    m "\"Shh, don’t get greedy! It’ll be harder on you if you try to force it.\""

    "I lower my restless hips, focusing on Myra’s touch, now little more than a gentle tease. I glance up at her through squinted eyes."

    "She grins down at me, her eyes thin with mischievous delight."

    "She begins to stroke me again, her bottom hand moving up and down with a rhythm that’s only a bit faster than outright teasing."

    "Her other circles the head of my cock, her fingers dancing around the tip."

    "I can feel the urge rising within me. Slower this time, more like the coming tide than the crash of a wave."

    "Myra seems to notice it too. Her fingers tighten around my shaft, and the teasing on my cockhead becomes an earnest demand."

    m "\"Don’t hold back. Let everything out this time~\""

    "I screw my eyes shut as I hit my limit. I let out a choked groan as I cum, my hips thrusting into Myra’s waiting grip."

    m "\"There you go!  Ah! It's so warm!\""

    "She giggles as my sticky seed dirties her hands. But she continues to stroke me as if trying to coax out every last drop."

    "It’s too good… I can’t think straight! Myra slows her pace as my climax reaches its peak and I let out one final spurt of cum."

    "I fall back against the bed, panting. I came so hard that my vision is blurring."

    m "\"Ahh! It’s all over my hair!\""

    "Myra rakes her fingers through her hair in a vain attempt to clean the mess I caused.  Finally realizing the hopelessness of the task, she looks down at her cum-soaked hands and eagerly licks her lips."

    m "\"Mnh...Hnn...\""

    "I don’t think I’ll ever be able to look at a grooming cat the same way ever again."

    "Myra’s deft tongue laps the streaks of cum from her hands, eliciting a moan with each eager lick."

    a "\"Myra, that was...\""

    m "\"Just what you needed, right?\""

    scene

    scene

    "Myra doesn't give me any time to rest.  With a face still red with pleasure, she slides off me and finishes wiping herself clean."

    #split dialogue depending on how Alex ended up at the village.

    m "\"Be sure not to mention anything to Taisa.  She'll be really really mad if she figures out we had so much fun behind her back.\""

    a "\"Somehow I don't think that's why she'd be mad.  She didn't seem too keen on us interacting at all.\""

    m "\"Oh, she's just no fun!  She doesn't like mother's rules, but she still goes along with them anyway.\""

    t "\"What else would I do?\""

    "Taisa enters carrying a basket of food, her tail swishing suspiciously behind her."

    t "\"Mother knows you won't listen to her. One whiff of the air in this room would tell her everything she wanted to know.\""

    a "\"Is it...uh... that obvious?\""

    "Taisa wrinkles her nose in disgust."

    t "\"Almost unbearable. Either you two have been screwing or you've been slapping Myra with a dead fish for the past half hour.\""

    a "\"That's-\""

    m "\"Hey~ I only used my hands! I saved the real fun for you!\""

    t "\"Alex, eat this food I brought before I vomit all over it.\""

    "Normally I'd never eat anything after hearing something so unappetizing, but after 6 months on a ship with nothing but hardtack and watery grog, I'll take anything I can get my hands on."

    "I take the basket of bread and dried meats from Taisa and dig in, munching down as she sits on a nearby stood."

    t "\"I hope you're feeling better now.  You've been asleep for almost three days.\""

    m "\"Maybe all he needed was a-\""

    t "\"Please don't finish that sentence.\""

    "As Taisa and Myra continue to bicker, I glance around the well-furnished room."

    a "\"I wasn't expecting you to bring me to a place like this.\""

    t "\"What?  Did you think we all lived in the trees?\""

    a "\"Well, I don't know what I thought.  I never really considered it.\""

    m "\"Maybe we can show him around, Taisa!\""

    t "\"Not today. Mother wanted to see him the moment he woke up.\""

    a "\"Your mother?\""

    t "\"The Queen. She said to bring you to see her, even if we had to drag you.\""

    "The Queen of the Jaguars... She just might be my ticket out of here."

    menu village_questions:

        "\"Tell me more about your mother.\"":
            jump lyra_explanation

        "\"Where did I wash ashore, anyway?\"":
            jump the_stripes

        "\"Do you think she might be able to help me?\"":
            jump visiting_the_queen





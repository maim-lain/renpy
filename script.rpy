define stu = Character ("Student", color="#BBCEBF")
define e = Character ("Elise", color="#FF5733")
define m = Character ("[name]", color ="AFABAA")
define v = Character ("Vanessa", color ="#5138B0")
define c = Character ("Chumee", color = "#34B44F")
define s = Character ("Stronk", color = "#B40E0E")
define h = Character ("Himia", color = "#53EAD7")
define l = Character ("Lou", color = "#E5253D")
define ef = Character ("Helirios", color ="#F5BA86")
define dai = Character ("Daimee", color ="#368528")
define lm = Character ("Lilian", color ="#852828")
define ukn = Character ("???", color ="#ffffff")
define Ele = Character ("Eleon", color ="#A1D3E4")
define o = Character ("Ophelia", color ="#3440CD")
define mi = Character ("Mine", color ="#80DE7D")
define doc = Character ("Delphine", color ="#1EB7A9")
define P = Character ("Principal", color ="#AEC740")
define mar = Character ("Marcus", color ="#3D1F37")
define vhead = Character ("Voice in your head", color ="#ffffff")
define arbiter = Character ("The Arbiter", color = "#83F2FF")
define Val = Character ("Valoria", color = "#FEFE92")
define ath = Character ("Athael", color = "#ADA7E2")
define flashbulb = Fade(0.2, 0.0, 0.8, color ='#fff')
default OLove = 0
default MLove = 0
default LLove = 0
default VLove = 0
default ELove = 0
default CLove = 0
default HLove = 0
default V01Intervene = False
default VTrustEliseBeach = False
default TaleWhiteMage = False
default TaleRedWidow = False
default NightEliseD3 = False
default ElenaBook = False
image vid = Movie(play = "EDream2.webm")
image vid B = Movie(play = "CMscene.webm")
image vid A = Movie(play = "CMCum.webm")
image vid C = Movie (play = "ENSFW1.mpg")
image vid D = Movie (play = "ENSFW2.mpg")
image vid E = Movie (play = "VLNSFW1.webm")
image vid F = Movie (play = "VLNSFW2.mpg")
image vid DI1 = Movie (play = "DI1.webm")
image vid DI2 = Movie (play = "DI2.webm")
image vid cd5 = Movie (play = "cd5.webm")
image vid cd52 = Movie (play = "cd52.webm")
image vid loud5 = Movie (play = "loud5.webm")
image vid loud52 = Movie (play = "loud52.webm")
default AngerD4 = False
default GFVD4 = False
default SRYHD4 = False
default Mcontrol = False
image vid G = Movie (play = "VNSFWD4.webm")
image vid H = Movie (play = "VNSFWD42.webm")
image vid I = Movie (play = "CCustom1.webm")
define mh = Character ("Mahamee", color ="#92ED1F")
define uknw = Character ("???", color = "#ffffff")
image vid CD3 = Movie(play = "CMShwrD3.webm")
default PeaceD1 = False
default ValoriaHelpD5 = False
default OverflowD5 = False
define config.menu_include_disabled = True
define Elefight = False
define EleKnow = False
define CVirginity = False
define fade = Fade(0.5, 2.0, 0.5)



label start:
    "WARNING"
    "This game contains content of a sexual nature."
    "You must be at least 18 years old to play this game."
    "By continuing you admit being legally allowed to play this game in your country."
    "Every character in this Visual novel is at least 18 or older."
    "The story is forged by the way you play it."
    "Some decisions might lock scenes or dialogues."
    "The music is also part of the story."
    "I recommend lowering the sound a bit for an optimized experience."

    play music "Mystery.mp3"

    "In 2030, humanity discovers that it wasn't the only intelligent race roaming the Earth."
    "To ensure priority on resources, humanity started a war against the other races, Elves, Dwarves, Goblins..."
    "They lost. The losses were insane.. more than a billion humans died, for millions of elves, goblins & dwarves."
    "5 Years of war ended in a bloodshed, where a hero, Athael stepped out to bring the war to an end."
    "This story takes place 20 years after the war..."
    "After the war mankind was reduced to slavery for the other races."
    "Humans below 20 were spared."
    "In 2050, Humanity is finally freed from slavery and forced labor, and is now as free as any other race."
    "But minds need time to change..."

    "And minds are easily altered."



    $ name = renpy.input("What's your name?").strip()

    "The world has been changed by the war..."
    "Hatred, vengeance, pride, love, everything and anything is a good reason to bring war upon a land."

    "You know it. Growing up on a farm, far from the issues of the world didn't change much for you, [name]."
    "But now your opinion matters..."

    "Will this ever change, will we one day be able to live in peace, every race, every mage?"


    menu:
        "What do you think [name]?"

        "Our world deserves peace.":
            $ PeaceD1 = True
            "You're thinking like a child, but maybe you're right."

        "Peace is unreachable, unreal.":
            "What a grim way to see your world, but maybe you're right."


    "..."

    stop music fadeout 1.0

    v "[name], [name] !"
    m "Uh.. what?"

    play music "FilledLove.mp3"

    scene vanessawup1
    v "Come on! We're gonna be late!"
    v "We don't want to be embarassed in front of the other races!"
    m "Alright, alright..."
    v "Thank you, I'll come back in 10 minutes."

    scene black
    m "(Even though Vanessa is quite demanding, I am glad she's around. Since my parents died during the Great War, she became my family.)"
    m "(My only family...)"
    m "(I wonder what I would be without her, without her mother's help when I was younger.)"
    m "Alright enough day dreaming."

    "10 minutes later.."

    scene vanessawup2
    v "I'm so excited, we are the first generation of humans to be allowed to Receive the same education as the other races!"


    menu:
        "Do I really care?"

        "I know right!":
            m "I know, right! Finally we are able to show the world what we are capable of doing!"
            v "I like your enthusiasm, come on, let's go!"
            $ VLove += 1

        "I mean...":
            scene vanessawup3
            m "I mean, let's be honest Vanessa, do you truly expect things to change?"
            v "They have to change, and if they don't we'll change them, quite being a spoilsport and let's get going!"


    scene black
    v "What do you think they will teach us [name]?"
    m "Hmm, I don't know maybe fire magic, arcane, frost ? the possibilities are endless!"
    v "Indeed, I'm really impatient!"

    scene VT1
    image VT1 = im.Scale("VT1.png", 1920, 1080)

    v "Here we are.."
    m "Indeed.."
    v "..."

    m "..."

    scene VT2
    image VT2 = im.Scale ("VT2.png", 1920, 1080)
    with fade

    v "W-well I guess we should try to-"
    with hpunch
    e "Look Chumee, humans!"

    scene EC
    image EC = im.Scale ("EC.png", 1920,1080)
    with fade

    e "I've never seen any of your kind here!"
    c "Calm down Elise, let them breathe."
    e "You're right, forgive my enthusiasm, I just am really curious about your kind."

    scene black fade
    scene EC Intro
    image EC Intro = im.Scale ("EC Intro.png", 1920, 1080)
    with fade

    e "I am Elise, I have been studying fire magic since my birth now !"
    e "I am 129-"
    with hpunch
    v " 129 ?! How can you be that old with such a young and beautiful face ?"
    e " Oh well, we elves don't age the same as you, I've always found sad that you humans can't live beyond 100 years old."
    e " If I'm right, in human years I am about ... 19 years old !"
    v " Oh I see, I'm Vanessa, I'm 20..."
    c " I'm Chumee, Chumee Grunbog, and I'm a Goblin... I mean I don't think you know any other race with that height and skin, I'm 19 years old as well."
    e " Glad to meet you Vanessa, and who is the person with you ?"


    menu:
        "How should I introduce myself "

        "Be polite":
            $ELove += 1
            m "The name is [name], I'm 20. Vanessa is a good friend, and I'm quite curious about everyone here."
            e "You seem calm [name], that will help here, I look forward to learning more about you!"
            c "Don't be afraid about being relaxed about it, you seem like a nice guy"

        "Be relaxed":
            $CLove += 1
            m "I'm [name], 20. Vanessa is a good friend, and I'm quite curious about everyone here."
            c "You sure know how to breath [name], I like it."
            e "I'm glad that we can all be so easygoing that early."


    scene black fade
    scene EC Talk
    image EC Talk = im.Scale("EC Talk.png", 1920,1080)

    e "We should probably get going"
    v "I agree, we should start visiting, [name]"

    e "Well me and Chumee can give you the tour, we've been around for a few hours now."
    m "Sure I could use some help, this place seems enormous!"

    if ELove >= 1:
        jump EliseV

    elif CLove >= 1:
        jump ChumeeV

    else:
        return



    label EliseV:

        e "Come [name], I'll be guiding you through, let's meet at the cafeteria around... 5PM"
        c "Sure."
        v "See you later then!"

        scene black
        "The Establishment is way bigger than it seems while still being classic, A library, courtyard, obviously, pool, club rooms."
        "Nothing that is out of the ordinary, basically a University.. but for magic."
        "After visiting the whole place with Elise, she stops."

        stop music fadeout 1.0
        scene ESerious
        image ESerious = im.Scale("ESerious.png", 1920,1080)


        e "I'm gonna be honest with you [name] you seem like a nice person, but not everyone here might think the same as me or Chumee."
        m "I expected that, I don't think I'll accepted after that early conflict."
        e "I'm Sorry [name].."
        menu :
            "..."
            "Compliment her":
                $ELove += 1
                m " Don't worry Elise, I don't need a lot of people to recognize me"

                m "I just want people I can count on, and you seem like that kind of person, I'm glad I met you."
                m "Maybe one day, everyone will forger about the past."
                m "But for now, there is a lot to do!"
                scene black
                scene ESmile
                image ESmile = im.Scale ("ESmile.png", 1920,1080)

                e " ... Thanks [name] that means a lot."
                e "Well, let's keep going, Vanessa and Chumee probably looking for us!"



                scene black

                e "Here we are, looks like they're already here..."

                scene black
                scene CafSmug
                image CafSmug = im.Scale ("CafSmug.png", 1920,1080)
                with fade

                v "You two took long enough, mind telling us what happened?"
                c "I didn't expect you to fall for the first human Elise!"
                e "N-no, I mean we took a lon-"
                c "Relax I'm just messing with you."



            "stay silent":
                m "..."
                e "..."
                e "Well, let's keep going, Vanessa and Chumee probably looking for us!"

                with fade

                scene black
                scene ECS
                image ECS = im.Scale ("ECS.png", 1920,1080)
                with fade

                e "Here we are, looks like they're already here.."

                scene black
                scene CafSmug
                image CafSmug = im.Scale ("CafSmug.png", 1920,1080)

                v "You two took long enough, mind telling us what happened?"
                c "I didn't expect you to fall for the first human Elise!"
                e "N-no, i mean we took a lon-"
                c "Relax i'm just messing with you"













        jump Reunion
    label ChumeeV:
        c "Come [name] I'll guide you through, Elise let's meet at the cafeteria afterward."
        e "Sure thing!"
        v "See you later then!"

        scene black fade
        scene CSerious
        image CSerious = im.Scale("CSerious.png", 1920,1080)
        stop music fadeout 1.0

        c "I'll be honest [name], Elise and I are quite open minded, but the majority here still despise humans."
        m "I expect that kind of opinion on humans..."



        c " Don't get me wrong, you look like a nice guy and I look forward to knowing more about you..."


        menu :
            "..."
            "Don't worry.":
                $CLove += 1
                m "Don't worry Chumee, I'm here to try new stuff, to find a new way to see life, and I alone am needed for that."
                m "Beside, I met you, and that's all that matters, I appreciate your honesty."

                scene black fade
                scene CReassuring
                image CReassuring = im.Scale("CReassuring.png", 1920,1080)

                c "I didn't expect you to take it that well. You're a cool guy [name], I'm glad I've met you too."
                c "Maybe you'll prove the other races wrong because of that."
                c "Alright, let's get going, I'm hungry!"


            "Remain silent":
                m "..."
                c "..."
                c "Well.. we should get going.."
                m "I agree."





        jump Reunion






    label Reunion:
        scene black
        scene CNormal
        image CNormal = im.Scale ("CNormal.png", 1920,1080)
        play music "FilledLove.mp3"


        v "This place sure is impressive!"
        v "But I wonder, how does class work?"
        v "We haven't been assigned to any class."

        scene CVETalk
        image CVETalk = im.Scale ("CVETalk.png", 1920,1080)


        e "Well, this place is for students, you can basically choose which class to attend."
        v "Oh I see, that's interesting"
        e "Have things been different in your schools? Before learning about us I mean."
        v "Well, I wasn't born yet, but my mother used to tell me about it."
        v "How she used to be classed in groups of students, following every class together."
        v "I wish I knew that time, but things have changed and... here we are!"
        e "A shame you'll never be able to experience it, but still, maybe learning our way can prove as good!"
        v "I hope so!"
        m "What kind of magic does this establishment teach, Elise?"
        with fade
        scene black
        scene CNormal2
        image CNormal2 = im.Scale ("CNormal.png", 1920,1080)
        e "Hmm it's my first year here, but if my memory is right?"
        e "Some will learn elemental magics, while others probably arcanes..."
        e "It really depends on what you enjoy, healing, protection, tech.."
        "A lot go through your mind, so many things that were usually in story books!"
        "Finally, something as specials as magic was within your range!"
        m "That's a lot!"
        c "Sure is, but I'm not into that magic nonsense, no I'm here for the pool, and the track field, and anything that involve sports basically."
        m "You do look fit..."
        c "Uh oh, he's a flirt~!"
        v "And you Eli-"





        with vpunch

        stop music

        stu "I WON'T TOLERATE IT !"

        scene black
        scene CBad
        image CBad = im.Scale ("CBad.png", 1920,1080)

        stu "I WON'T SHARE MY CLASS, WITH THOSE DISGUSTING, FILTHY, DUMB HUMANS!"
        scene black
        scene StuC
        image StuC = im.Scale ("StuC.png", 1920,1080)
        stu "That's a disgrace, sharing our ancient knowledge with those monkeys!"
        stu "I won't stand by and let that happen Himia!"
        scene black
        scene HimiaInter
        image HimiaInter = im.Scale ("HimiaInter.png", 1920,1080)
        h "You need to learn respect, brother."
        h "Give them a chance, and please..."
        h "Stop screaming for no reason."
        h "You know I don't like it!"
        stu "Hmpf..."



        menu :
            "He's starting to get on my nerves.."
            "Intervene":
                $V01Intervene = True
                $CLove += 1
                with hpunch
                scene black
                scene CInter
                image CInter = im.Scale ("CInter.png", 1920,1080)

                v "{size=-10} Don't move, [name] stay calm !{/size}"

                scene black
                scene StuLeave
                image StuLeave = im.Scale ("StuLeave.png", 1920,1080)
                "With all his might, the student engages in a graceful, and yet hateful walk to the corridor."

                stu "{size=-10} Disgusting apes... {/size}"
                scene CInter
                image CInter = im.Scale ("CInter.png", 1920,1080)

                c "You're quite bold [name], I like my men bold."
                v "Don't be that easily triggered [name] we're past that !"
                e "I agree, let it slide, things will change eventually."
                c "Meh, I mean, he has some balls better use em' right?"
                "You look at Chumee, as her mouth slowly draws a smug."
                e "Anyway, let's move, the visit is over and class only begins this Monday."


                jump ChumeeD


            "I'll prove them wrong..":
                $V01Intervene = False
                $VLove += 1
                $ELove += 1
                scene black
                scene CAmbition
                image CAmbition = im.Scale ("CAmbition.png", 1920,1080)

                m "{size=-10} I'll prove them wrong. {/size}"
                scene black
                scene StuLeave
                image StuLeave = im.Scale ("StuLeave.png", 1920,1080)

                stu "{size=-10} Disgusting apes... {/size}"
                scene black
                scene CAmbition
                image CAmbition = im.Scale ("CAmbition.png", 1920,1080)
                with fade
                v "I'm glad you stood silent [name] we don't need to draw attention.."
                e "I'm sure you'll prove them wrong [name].."
                c "I would've put that damn elf back in his place if i were you, [name].."
                e "Anyway, let's move, the visit is over and class only begins this Monday."


                jump ChumeeD




            "Remain Silent..":
                $V01Intervene = False

                scene black
                scene StuLeave
                image StuLeave = im.Scale ("StuLeave.png", 1920,1080)

                stu "{size=-10} Disgusting apes... {/size}"


                scene black
                scene CBad
                image CBad = im.Scale ("CBad.png", 1920,1080)

                v "That was.. depressing to listen to.."
                e "Don't worry you two, those are just words, one day things will change."
                c "I would've put that damn elf back in his place."
                e "Anyway, let's move, the visit is over and class only begin this Monday."

                jump ChumeeD

    label ChumeeD:

        play music "FilledLove.mp3"

        scene black

        c "Alright, that was nice, but I've got to workout, so I guess we're splitting up here"
        e "Sure Chumee, see you tomorrow."
        v "See ya'!"
        c "..."

        "Elise & Vanessa step outside waiting for you"


        scene Csad
        image Csad = im.Scale ("Csad.png", 1920,1080)

        c "[name].. I know how being insulted that way must've felt, but please don't think we are all like that.."
        m "Chumee, you're your own proof, you and Elise proved yourself to be really friendly despise all that happened in the past."
        m "Don't worry about me I'm just glad me and Vanessa met you two."
        scene black
        scene Ctalk
        image Ctalk = im.Scale ("Ctalk.png", 1920,1080)

        c "You're a nice person [name].."
        c "Alright, I should get going!"

        menu :
            "Should I add something ?"
            "Flirt with her":
                $CLove += 1

                m "I like girls who workout."
                scene black
                scene Cflirt
                image Cflirt = im.Scale ("Cflirt.png", 1920,1080)
                c "Well maybe I was meant for you then."
                m "See you chumee."
                c "Bye Handsome!"
                jump evening
            "Wave back":
                m "Sure, see you tomorrow!"
                c "Bye [name]!"
                jump evening

    label evening:

        scene black
        scene EVTalk
        image EVTalk = im.Scale ("EVTalk.png", 1920,1080)

        e "By the way [name], Vanessa. I am going to the beach with Chumee tomorrow, you two should come !"
        v "The beach you say? Sure! Why not!"
        e "Great! By the way where do you two live?"
        m "Oh, we live to the east of the establishement, fifteen minutes at most."

        scene black
        scene EVSmile
        image EVSmile = im.Scale ("EVSmile.png", 1920,1080)


        e "Oh we're near then, let's go home together !"

        if ELove >=2:
            "Wow.. Elise has a beautiful smile.."
            "Everything is beautiful, the sunset, the trees, her.."
            "Put it back together [name], you're a human, she's an amazing Elf, there is no way that could work.."

            v "Sure thing Elise!"
        else:
            jump backhome

    label backhome:

        v "Sure thing Elise!"


        scene black
        with fade
        scene EVWalk
        image EVWalk = im.Scale ("EVWalk.png", 1920,1080)

        v "I can't wait to learn new things!"
        e "I've never seen humans using mana."
        e "If anything that'll be interesting to see."

        if V01Intervene == False:
            jump Silent

        else:
            jump Intervene

    label Intervene:
        scene black
        scene EVScold
        image EVScold = im.Scale ("EVScold.png", 1920,1080)

        e "I know that such comments are not pleasent to hear [name], but you must remain calm. Things will change, in time..."
        e "I'm sure you and Vanessa will play a major role in your race's history."
        v "She's right you know! Of course we won't be accepted right away..."
        v "You need to control yourself."
        m "..."

        with fade

        hide EVScold
        scene black

        jump home

    label Silent:

        scene black
        scene EVproud
        image EVproud = im.Scale ("EVproud.png", 1920,1080)
        e "By the way [name].."
        e "I'm glad you didn't act when that elf started insulting your kind. Ignoring him was the right thing to do, you're better than him."
        v "Definitely, I expected you to jump out of your chair and try to mess that elf up."
        v "Your cold blood impressed me."


        jump home



    label home:


        scene black


    "After a few minutes of walking, talking about anything and everything, you finally reach your place."
    scene black
    scene Home
    image Home = im.Scale ("Home.png", 1920,1080)
    v "Well here we are !"
    v "Home.."
    scene black
    scene Ebye1
    image Ebye1 = im.Scale ("Ebye1.png", 1920,1080)



    e "Well I live just around the corner, we are indeed really close!"
    e "See you two tomorrow, I'll come and get you in the morning."

    v "See you Elise!"
    m "Bye!"

    if ELove >= 3:
        scene black
        scene ECall
        image ECall = im.Scale ("ECall.png", 1920,1080)
        with fade
        e "Oh and [name]!"
        m "Yeah ?"
        scene black
        scene ELove
        image ELove = im.Scale ("ELove.png", 1920,1080)
        with fade
        e "I am glad I've met you too.."

    elif ELove >= 2:
        scene black
        scene ECall
        image ECall = im.Scale ("ECall.png", 1920,1080)

        with fade
        e "Oh and [name]!"
        m "Yeah ?"
        scene black
        scene ELove
        image ELove = im.Scale ("ELove.png", 1920,1080)

        with fade
        e "I look forward to knowing more about you."


    else:
        jump dinner

label dinner:

    "."
    ".."
    "..."

    v "Come on now, [name]"
    v "Do you really think you can fool me like that?"

    scene black
    scene Vsmug
    image Vsmug = im.Scale ("Vsmug.png", 1920,1080)

    if ELove >= 3:


        v "First, you decide to remain calm where you would've usually exploded"
        v "Then you look at her as if she was the only girl in your life !"

        menu :

            "She is beautiful":
                $VLove += 1



                m "She is.. something, but how could I attract an Elf, she looks amazing, strong and all..."
                m "While I'm just .. well [name]!"
                scene black
                scene VReassure
                image VReassure = im.Scale ("VReassure.png", 1920,1080)
                v "Moh, don't worry [name] you're way more than that, I know it!"
                m "Thanks Vanessa, I wonder what would I be without you"
                v "I don't know, but I am glad to be at your side"
                jump bed

            "Are you jealous ?":
                $VLove += 2
                m "Sorry, didn't meant to make you jealous"
                scene black
                scene Vblush
                image Vblush = im.Scale ("Vblush.png", 1920,1080)
                v "W-What ?"
                m "Don't worry, you'll always have your place in my heart Vanessa"
                v "I-I mean I'm not jealous or anything... I'm just glad for you..."
                scene black
                scene Vheart
                image Vheart = im.Scale ("Vheart.png", 1920,1080)
                v "But thanks [name], you too have your own special place deep down"
                v "I'm happy to be with you."
                jump bed


    elif CLove >= 3:

        v "That goblin couldn't keep her eyes off you! You made quite the impression on her!"
        v "I didn't knew you were into smaller girls [name].."

        menu :

            "She's refreshing":
                $VLove += 1
                m "Chumee is interesting and, I've never seen a gobelin before.. and who knows!"
                m "But she is a fit person, smiling on life..."
                m "While I'm just .. well [name]!"
                scene black
                scene VReassure
                image VReassure = im.Scale ("VReassure.png", 1920,1080)
                v "Moh, don't worry [name] you're way more than that, I know it!"
                m "Thanks Vanessa, I wonder what would I be without you"
                jump bed

            "Are you jealous ?":
                $VLove += 2
                m "Sorry, didn't meant to make you jealous."
                scene black
                scene Vblush
                image Vblush = im.Scale ("Vblush.png", 1920,1080)
                v "W-What ?"
                m "Don't worry, you'll always have your place in my heart Vanessa."
                v "I-I mean I'm not jealous or anything... I'm just glad for you..."
                scene black
                scene Vheart
                image Vheart = im.Scale ("Vheart.png", 1920,1080)
                v "But thanks [name], you too have your own special place deep down."
                v "I'm happy to be with you."
                jump bed



    else:
        v "How's the food ?"
        menu :
            "..."
            "Great as always":
                $VLove += 1
                m "Great as always Vanessa."
                v "I'm glad I got something from my mother then"
            "It's alright":
                m "Well it's alright i guess."
                v "Is it that bad ?"
                m "No, not really, it's just, the same thing as every other day"

                jump bed

    label bed:



        scene black
        scene VNight
        image VNight = im.Scale ("VNight.png", 1920,1080)

        v "Well it's getting late, we should sleep early!"
        v "I don't want to be late tomorrow!"
        m "You're right, beside I could use the rest."
        m "Good night Vanessa."
        v "Sweet dreams [name]."

        scene black
        with fade

        stop music

        ".."
        "..."

        "Don't resist [name]..."
        "I know... what you want..."

        if VLove >= 3:
            "Is it that cute childhood friend of yours?"

            scene black
            scene VNSFWD1
            image VNSFWD1 = im.Scale ("VNSFWD1.png", 1920, 1080)
            with fade

        else:
            jump Elisensfw

    label Elisensfw:

        if ELove >= 3:
            "That impressive elf you met today?"
            scene black
            scene ENSFWD1
            image ENSFWD1 = im.Scale ("ENSFWD1.png", 1920, 1080)
            with fade
        else:
            jump Chumeensfw

    label Chumeensfw:

        if CLove >= 3:
            "That small teasing goblin?"
            scene black
            scene CNSFWD1
            image CNSFWD1 = im.Scale ("CNSFWD1.png", 1920, 1080)
            with fade
        else:
            jump Know

    label Know:
        "You'll get them with my power"
        scene black
        show VN
        image VN = im.Scale ("VN.png", 1920,1080)
        with fade

        "They will submit"
        hide VN
        show VEN
        image VEN = im.Scale ("VEN.png", 1920,1080)
        with fade

        "To you"
        hide VEN
        show VECN
        image VECN = im.Scale ("VECN.png", 1920,1080)
        with fade

        "And you alone."
        hide VECN
        jump Day2

    label Day2:

        play music "Mystery.mp3"

        "We are closer than you think, [name]."
        "Meeting that elf was your destiny..."
        m "What do you mean? Who are you?"
        "You'll soon know, [name]."
        "Know that everything you know is a lie."
        m "A lie?"
        "You're not a mere human, [name]..."
        "You have a purpose, a huge burden will soon be on your shoulders."
        "Be ready."
        "..."

        with vpunch
        stop music fadeout 1.0
        "*Knock* *Knock*"

        v "[name] ... can I come in?"
        m "Sure just let me put something on."
        "..."

        play music "FilledLove.mp3"

        scene black
        scene Vask
        image Vask = im.Scale ("Vask.png", 1920, 1080)

        m "So... How can I help?"
        v "Have you already seen the sea, [name]?"
        m "Well, before joining your mother's farm, I used to live near a beach."
        v "Can I ask you something a bit... embarassing?"
        m "Shoot."
        v "Well... I've never seen the sea, and never learned to swim..."
        v "Can you please train me once we get there?"

        menu :
            "..."
            "Sure.":
                $VLove += 3
                m "Sure!"
                v "Really?"
                m "I mean why not, it would be a shame for you to not be able to swim."
                scene black
                scene Vyes
                image Vyes = im.Scale ("Vyes.png", 1920, 1080)
                with fade
                v "Thanks [name]!"
                v "You're the best!"
                m "No worries Vanessa, come on, let's get dressed, Elise must be waiting for us!"
                v "You're right!"
                jump Elise2
            "We'll see":
                $VLove += 1
                m "I don't know if I will be able to Vanessa..."
                scene black
                scene Vno
                image Vno = im.Scale ("Vno.png", 1920, 1080)
                with fade
                v "Oh... I-I see"
                v "That was dumb of me to ask"
                m "I'll see if I can train you alright?"
                m "I am not even sure that I remember proprely how to swim myself."
                v "Okay... don't worry"
                m "Come on, let's get dressed, Elise must be waiting for us."
                v "You're right..."
                jump Elise2

    label Elise2:
        scene black
        scene Egreet
        image Egreet = im.Scale ("Egreet.png", 1920, 1080)
        with fade

        e "[name], you came!"
        m "Hey Elise, how are you?"
        e "Fine as always."

        scene black
        scene Equestion
        image Equestion = im.Scale ("Equestion.png", 1920, 1080)
        with fade
        e "Where is Vanessa?"

        scene black
        scene VSea
        image VSea = im.Scale ("VSea.png", 1920, 1080)
        with fade

        m "Looking at the sea, she never saw it with her own eyes."
        e "Oh... that's quite sad."
        menu :
            "..."
            "Be Hopeful":
                $ELove += 1
                m "Don't be..."
                m "On the contrary, she is finally able to see it."
                m "And I'm sure she's happy to stand here."
                scene black
                scene Egreet
                image Egreet = im.Scale ("Egreet.png", 1920, 1080)
                with fade
                e "Well, you do have the words to turn things in a positive way!"
                scene black
                scene VSea
                image VSea = im.Scale ("VSea.png", 1920, 1080)
                with fade
                m "VANESSA!"
                with hpunch

                jump EVBeach

            "Just, call Vanessa":
                m "VANESSA!"

                jump EVBeach
    label EVBeach:
        scene black
        scene VSorry
        image VSorry = im.Scale ("VSorry.png", 1920, 1080)
        with fade

        with vpunch
        v "SORRY!"

        scene black
        scene EVGreet
        image EVGreet = im.Scale ("EVGreet.png", 1920, 1080)
        with fade

        v "Sorry, I lost myself in my own thoughts."
        v "How are you Elise?"
        e "I'm doing great thanks for asking."
        e "Don't worry, I too would be excited watching the beach for the first time!"

        scene black
        scene EV2
        image EV2 = im.Scale ("EV2.png", 1920, 1080)
        with fade

        e "Anyway, Chumee will be a little late, she will join us a bit later."
        e "Let's just sit for a moment while we wait for her."

        scene black
        scene EVB
        image EVB = im.Scale ("EVB.png", 1920, 1080)
        with fade

        v "This place is amazing!"
        v "I've never seen such a sunny place."
        v "The hot sand, the fresh air, the noise of the waves..."
        e "I agree, I used to live around one with my..-"

        scene black
        scene EVS
        image EVS = im.Scale ("EVS.png", 1920, 1080)
        with fade
        v "Are you okay Elise?"
        v "I'm sorry if I said something that I wasn't supposed to..."

        e "D-don't worry Vanessa, it's ok."

        scene black
        scene EVS2
        image EVS2 = im.Scale ("EVS2.png", 1920, 1080)
        with fade

        e "*sigh*"
        e "Just painful memories, but I'm fine, the weather is great."

        if ELove >= 3:
            e "I'm glad to be with you two."

        elif ELove >= 2:
            e "I'm happy to be here"

        else:
            jump ChumeeB

    label ChumeeB:
        scene black
        scene Chi
        image Chi = im.Scale ("Chi.png", 1920, 1080)
        with fade

        c "Hey Elise, [name], Vanessa!"
        e "Hey Chumee, you came all the way wearing... this?"
        c "Well yes, and [name] seems to like it!"
        c "Can't blame him, though~."

        menu :
            "..."
            "Play along":
                $CLove += 1
                m "Guilty. what kind of fool would be disgusted by this sight?"
                c "See?"
                e "I guess..."
                v "Yeah..."
                jump Beach
            "Break her out of her bubble":
                m "Sorry Chumee, but it doesn't do much to me."
                c "Meh, you're no fun [name]."
                c "Can't even be honest about his pervy thoughts."
                jump Beach
    label Beach:

        scene black
        scene CBeach
        image CBeach = im.Scale ("CBeach.png", 1920, 1080)
        with fade

        e "Alright, we're all here, we should move!"
        v "I agree, the waves have been calling me for a while now!"



        scene black

        "10 minutes later"

        scene VCPlay
        image VCPlay = im.Scale ("VCPlay.png", 1920, 1080)
        with fade

        m "(I missed this feeling.)"
        m "(Sitting on the sand, feeling the hot embrace of the sun on my skin.)"

        m "(Still there is one thing I don't understand...)"

        scene black
        scene Ehide
        image Ehide = im.Scale ("Ehide.png", 1920, 1080)
        with fade

        m "Why are you hiding your body?"
        e "I-I just don't like it."

        menu :
            "..."
            "Comfort her":
                $ELove += 3
                m "Elise, you're not thinking that are you?"
                e "Why not... elves are despicable, to look at and to listen to."
                m "But are you?"
                m "You've been adorable since the second we met."
                m "Friendly and yet, really curious about my kind."
                m "My kind is to blame for everything terrible that happened on this Earth..."
                m "I should be ashamed."
                scene black
                scene EThink
                image EThink = im.Scale ("EThink.png", 1920, 1080)
                with fade
                e "No... [name]... your kind is not to blame."
                e "It never was..."

                jump Truth


            "Remain Silent":
                m "..."
                scene black
                scene EThink
                image EThink = im.Scale ("EThink.png", 1920, 1080)
                with fade
                e "I'm sorry, a lot has been happening lately..."

                jump Truth

    label Truth:



        e "[name]... Everything you know is a lie."

        stop music fadeout 1.0

        m "(Wait, I remember that sentence...)"
        play music "Mystery.mp3"
        scene black
        "Everything you know is a lie."
        scene Eexplain
        image Eexplain = im.Scale ("Eexplain.png", 1920, 1080)
        with fade

        e "Humanity never waged war against any races."
        m "W-what do you mean, we have books, and people telling stories about it."
        m "I even remember my parents leaving me to fight!"
        m "I remember the human propaganda spread across the cities..."
        m "How could it be a lie?"
        m "(What Elise is telling me makes no sense...)"
        m "(And yet it does coincide with my dream...)"
        m "(Maybe her warning should be taken seriously.)"

        scene black
        scene Esad
        image Esad = im.Scale ("Esad.png", 1920, 1080)
        with fade


        e "I don't have any proof yet [name]... I have a few memories, but everything is really..."
        e "Blurry."
        e "But I am certain of it, this war is a lie."

        menu :
            "Should I trust her?"
            "I trust you.":
                $ELove += 2
                m "I trust you Elise."
                $VTrustEliseBeach = True
                scene black
                scene EO
                image EO = im.Scale ("EO.png", 1920, 1080)
                with fade
                m "You have been nothing but good to me since we first met."
                m "Beside I have my own reasons to doubt that war as well..."
                e "R-Really?"
                m "Yeah."

                stop music fadeout 1.0


                scene black
                scene ETrust
                image ETrust = im.Scale ("ETrust.png", 1920, 1080)
                with fade

                play music "FilledLove.mp3"

                e "Finally!"
                e "I thought I would loose you too!"



                if ELove >= 8:
                    e "You're definitely the one I was looking for!"
                    e "I am so happy to have you!"
                else:
                    jump VaBeach




            "I need more time.":
                scene black
                scene Eunderstand
                image Eunderstand = im.Scale ("Eunderstand.png", 1920, 1080)
                with fade

                m "That seems, insane for me Elise, I think  will need time to process that."

                stop music fadeout 1.0


                e "I-I understand, it seems unreal..."

                play music "FilledLove.mp3"
                m "Yeah... a bit, although I don't feel like you're wrong..."
                m "And you have no reasons to lie to me."

                jump VaBeach

        label VaBeach:


            scene black
            scene VBask
            image VBask = im.Scale ("VBask.png", 1920, 1080)
            with fade

            v "Soooo... [name], can you teach me how to swim?"
            m "I'd love to but Elise and-"
            e "Don't worry, I'll be fine."
            e "Beside I could use some time alone."

            m "Well, I guess I'm teaching you how to swim Vanessa."

            scene black
            scene Vok
            image Vok = im.Scale ("Vok.png", 1920, 1080)
            with fade
            $VLove += 1

            v "Thanks [name], come on!"
            v "I can't wait."

            scene black

            v "Oh god, that's it, I'm sinking!"
            m "Vanessa."
            v "That was a dumb idea [name] I'm sorry!"
            m "Vanessa."

            scene VPanic
            image VPanic = im.Scale ("VPanic.png", 1920, 1080)
            with fade

            m "You realise I can still touch the ground?"
            v "Then keep holding me!"
            v "I need to swim I've always dreamed of it!"

            scene black
            scene VHBack
            image VHBack = im.Scale ("VHBack.png", 1920, 1080)
            with fade

            m "..."
            v "Why are you so silent?!"

            scene black
            scene VHA
            image VHA = im.Scale ("VHA.png", 1920, 1080)
            with fade

            m "I'm already holding you."
            v "Wait... you are."

            scene black

            "You spend a few hours trying to teach Vanessa how to be relaxed"
            "Without any success."

            scene VBSad
            image VBSad = im.Scale ("VBSad.png", 1920, 1080)
            with fade

            stop music fadeout 1.0

            v "I'm sorry [name]..."
            v "You have wasted your time, because of me..."
            v "I can't seem to be even decent in any discipline."
            v "Elise, Chumee, they're so much better than me."
            v "Why would you enjoy your time with me?"
            v "I'm useless."

            play music "Blackbird.mp3"

            menu :
                "..."
                "That's not true":
                    $VLove += 3
                    scene black
                    scene VBSad
                    image VBSad = im.Scale ("VBSad.png", 1920, 1080)

                    m "That's not true."

                    scene black
                    scene MCReassure
                    image MCReassure = im.Scale ("MCReassure.png", 1920, 1080)

                    m "You've always been around when I needed help."
                    m "You never let me down, even when I moved from your mother's farm."
                    m "You stuck with me against her will."
                    m "Having a few issues with swimming doesn't make you useless or incompetent."
                    m "I don't want to give you up just because we met them."

                    scene black
                    scene VHB
                    image VHB = im.Scale ("VHB.png", 1920, 1080)
                    with fade

                    v "You really think so?"
                    m "Absolutely."
                    v "Thanks [name]."
                    v "Thanks for being you."
                    if VLove >= 6:
                        v "You're really important to me."
                        v "I don't want you to forget about me."
                        m "That won't happen."
                        v "I'm glad!"
                        jump depart3
                    else :
                        jump depart3





                "Stay silent":
                    jump depart3

        label depart3:
            scene black
            scene CVBeach1
            image CVBeach1 = im.Scale ("CVBeach1.png", 1920, 1080)
            with fade
            c "Well, that was a fun day!"
            v "It sure was, I'm kind of exhausted though."
            c "Same, guess I'll head back now!"
            v "Me too... I could use some time alone."
            scene black
            scene CVBeach2
            image CVBeach2 = im.Scale ("CVBeach2.png", 1920, 1080)
            e "That was nice, I'll stay here, I love looking at the sun slowly setting."
            scene black
            scene CVBeach3
            image CVBeach3 = im.Scale ("CVBeach3.png", 1920, 1080)
            with fade
            menu :
                "Who am I staying with?"
                "Accompany Chumee":
                    $CLove += 2
                    m "I'll go with you Chumee."
                    c "Sure, I could use a handsome human on my way back home."
                    e "See you [name], thanks for listening to me!"
                    jump ChumeeR
                "Stay with Elise":
                    $ELove += 2
                    m "I'll stay with Elise"
                    c "I see that you're a commited lover [name]!"
                    c "Lucky you Elise."
                    e "See you Chumee!"
                    c "See you two later!"
                    jump EliseR


        label EliseR:

            scene black
            scene EThink2
            image EThink2 = im.Scale ("EThink2.png", 1920, 1080)

            e "It's beautiful... Isn't it?"
            e "I always loved the sunset. Feeling the warm embrace of the sun."
            e "Before facing the cold night."
            jump ERomance



        label ERomance:



            scene black
            scene Eflirt1
            image Eflirt1 = im.Scale ("Eflirt1.png", 1920, 1080)
            with fade


            if ELove >= 8:
                e "I guess I won't feel that cold with you next to me."
                e "... You and I, I feel like we got already so close, In so little time."
                scene black
                scene MCBadThing
                image MCBadThing = im.Scale ("MCBadThing.png", 1920, 1080)
                with fade
                m "Is that a bad thing?"
                scene black
                scene ELaugh
                image ELaugh = im.Scale ("ELaugh.png", 1920, 1080)
                with fade
                e "Not at all!"
                e "On the contrary!"
                scene black
                scene ELove2
                image ELove2 = im.Scale ("ELove2.png", 1920, 1080)
                with fade
                e "You've been perfect."
                e "Remaining silent in the face of adversity."
                e "Being kind and comprehensive with me."
                e "You stood with me when you knew I needed someone."
                e "..."
                scene black
                scene ESmileB
                image ESmileB = im.Scale ("ESmileB.png", 1920, 1080)
                with fade
                e "I feel things that I never felt before when you're near me [name]..."
                e "I don't know if it's ..."
                e "Nevermind."
                e "I'm just glad you're with me right now."
                jump ESunset
            else :
                e "Thank you for sticking with me."
                e "I definitely didn't wanted to remain alone after what we talked about."
                jump ESunset

        label ESunset:

                if VTrustEliseBeach == False:
                    jump EHome

                else :
                    e "Thank you [name]..."
                    m "For what?"
                    e "Trusting me."
                    jump EHome
        label EHome:

            scene black
            "You spend your time with Elise."
            "You both seem to have a good time."
            "She seems to like you more..."

            scene black
            scene EHome
            image EHome = im.Scale ("EHome.png", 1920, 1080)
            with fade

            e "It's getting late, we should head back home."
            m "(Elise and I grew closer over the last few days, Should I ask her on a date?)"

            menu :

                "Ask Elise on a date" if ELove >= 8:
                    m "Well, Elise..."
                    m "We grew closer quite quickly, and..."
                    m "I-I wonder maybe we should."
                    m "Spending some more time together..?"
                    scene black
                    scene EDP
                    image EDP = im.Scale ("EDP.png", 1920, 1080)
                    with fade
                    e "You're cute [name], I'd love to go on a date with you!"
                    scene black
                    " You finally go back home with Elise, you're trying to hide your joy."
                    " She seems to have noticed it"

                    jump ScenesD2
                "Back out":
                    m "You're right let's go..."
                    jump ScenesD2

        label ChumeeR:
            scene black
            scene CTalkB
            image CTalkB = im.Scale ("CTalkB.png", 1920, 1080)
            with fade
            c "I'm sorry, I didn't really spend time with you today."
            m "Why?"
            scene black
            scene CAvert
            image CAvert = im.Scale ("CAvert.png", 1920, 1080)
            with fade
            c "It's a bit complicated..."

            menu :

                "Ask anyway" if CLove >= 5:
                    $CLove += 2
                    c "Well, you see..."
                    c "Goblins have... heat issues."
                    m "Heat issues?"
                    c "Heat issues."
                    jump CHeat
                "Don't put your nose in her business":
                    scene black
                    scene CUnder
                    image CUnder = im.Scale ("CUnder.png", 1920, 1080)
                    with fade
                    $CLove += 1
                    m "I'm sure you have some good reason Chumee."
                    c "Thanks... for understanding [name]."
                    scene black
                    "You spend some time with Chumee while going back Home."
                    "She seems to like you more!"
                    "..."
                    "You finally get home"
                    jump ScenesD2

        label CHeat:
            scene black
            scene CTHeat
            image CTHeat = im.Scale ("CTHeat.png", 1920, 1080)
            with fade
            m "You mean Like... sexual heat issues?"
            c "Yeah."
            c "That..."
            c "It just feels, like..."
            c "A wave, I can't help it, it's beyond control!"
            m "I see, but why did that kept you from me?"
            c "Well, we usually take some pills or medication to, you know..."
            c "Control our needs"
            c "But I was out in the morning, I-I kind of wanted to..."
            m "To...?"
            c "I wanted to see you. There I said it!"
            m "Just to see me?"
            c "... No, I have something a bit personnal to ask you..."
            m "Go ahead, I won't judge you."
            c "W-Well, I need some help with those Heat problems..."
            m "Well, I care about you and If I can help I'll do it!"
            scene black
            scene Croute
            image Croute = im.Scale ("Croute.png", 1920, 1080)
            with fade

            c "I'm sure you would, what kind of fool would reject a cute and hot Goblin like me?"
            m "I can get behind that."
            m "(Did I just agreed on hooking up with Chumee?)"
            c "You might get behind a lot in the days to come!"
            c "But anyway, let's get home I'm exhausted!"
            scene black
            "You spend some time with Chumee while going back Home."
            "She seems to like you more!"
            "..."
            "You finally get home."
            jump ScenesD2


        label ScenesD2:

            scene black
            scene MCBackHome
            image MCBackHome = im.Scale ("MCBackHome.png", 1920, 1080)
            with fade

            v "Oh, you're back!"
            v "Sorry I already ate, I've saved a plate for you though, on the table."
            v "I-I'm a bit exhausted, so I'll just shower and head to bed."
            m "Sure I guess."
            v "Well sweets dreams!"
            m "Night!"
            scene black
            stop music fadeout 1.0

            "The evening is quiet, you spend some time in your room before heading to bed..."
            "..."
            with vpunch

            scene black
            scene BlurryR
            image BlurryR = im.Scale ("BlurryR.png", 1920, 1080)
            with fade

            m "W..what?"
            "Finally !"
            "Freedom !"
            scene black
            scene RRoom
            image RRoom = im.Scale ("RRoom.png", 1920, 1080)
            "After all these years, I can finally take a human form!"
            m "Who... Who said that?"

            play music "Rain.mp3"

            scene black
            scene LouFreed
            image LouFreed = im.Scale ("LouFreed.png", 1920, 1080)
            with fade

            l "Ah! The sweet feeling of freedom!"

            scene black
            scene LouIntroduction
            image LouIntroduction = im.Scale ("LouIntroduction.png", 1920, 1080)
            with fade
            l "Shame it's already so dark, I miss the sun..."
            m "..."
            l "Oh and you must be [name], nice to finally meet you!"
            l "I thought you would be taller though."
            scene LouQScreen
            image LouQScreen = im.Scale ("LouQScreen.png", 1920, 1080)
            with fade

            l "You probably have a lot of questions, go ahead I'll answer them."
            jump QLou1

        label QLou1:

            menu :

                "Who are you ?":

                    scene LouIntroduction
                    image LouIntroduction = im.Scale ("LouIntroduction.png", 1920, 1080)
                    with fade
                    l "Well, my name is Louise, although you can call me Lou."
                    l "I'm a half Succubus."
                    jump QLou1

                "Where do you come from?":


                    scene LouPast
                    image LouPast = im.Scale ("LouPast.png", 1920, 1080)
                    with fade
                    l "Well that's quite a long story, but long story short..."
                    l "I was born from a loving father and a Succubus, my mother."
                    l "It also explains my body type... Succubi usually absorb vital energy from sexual intercourses."
                    l "Giving life to new succubi, ready to do the same... but not me."
                    l "I was born from love, and I was missing vital force which explains my body."
                    m "That actually sounds... wholesome."
                    l "Give me a break... but still, I'm glad you asked."
                    jump QLou1

                "Continue.":
                    $LLove += 1
                    jump LouIntro

        label LouIntro:

            scene LLeave
            image LLeave = im.Scale ("LLeave.png", 1920, 1080)
            with fade
            l "Anyway we'll talk more about it tomorrow..."
            m "But I have so many questions!"
            l "You'll have to wait, [name] it's my first appearance in the physical world."
            m "But you said you knew your parents! How can it be your 'first appearance'?"
            l "You're hard to let go, aren't you?"
            l "Tomorrow, you'll have your answers, I promise."
            m "And Vanessa, she probably heard us!"
            l "Don't worry, this red aura around us is sealed, no one can hear us."
            l "Either way, have a good one [name] and remember..."

            stop music fadeout 1.0
            scene black

            l "Everything you know is a lie."
            l "This elf... she knew what she talked about."

            "..."
            "... You feel your strengh leaving you as you fall back on your bed."
            "Elise & Lou's voices seems like one and you hear one last time from both of them."
            "Everything is a lie."
            jump NSFWD2

        label NSFWD2:
            "..."
            "..."








            if ELove >= 8:
                with vpunch
                scene vid
                with fade
                m "Elise... I-I love you!"
                e "I love you too [name]"
                e "I wanted this to happen for so long!"
                e "Just you and me, connected..."
                e "Relax now, it's just the two of us."
                e "Let me take care of you..."
                "..."
                scene black
                scene EWup1
                image EWup1 = im.Scale ("EWup1.png", 1920, 1080)
                with hpunch

                e "Wh..What..."
                scene black
                scene EWup2
                image EWup2 = im.Scale ("EWup2.png", 1920, 1080)
                with fade
                e "What a ...mmm... Dream."
                e "... [name]..."


                jump past1

            elif CLove >= 6:

                scene black
                c "Fuck... this heat is fucking unbearable..."
                scene vid A
                c "I can't breath for 5 minutes without.. ah fuck! Needing that."
                c "It's ... fucking annoying, and yet it feels so good..."
                c "... Fuck ... [name]... I want... you..."
                c "... I need something... or else I'm gonna go crazy..."
                c "Shit! I can feel it coming!"

                scene vid B
                c "Ffffuuuucck..."
                c "..."
                c "Fuck... that was..."
                c "Intense..."
                c "I need... [name]..."
                scene black
                with fade
                jump past1

            else:
                jump past1

        label past1:
            scene black
            stop music fadeout 1.0
            "..."
            play music "Ambition.mp3"

            "30 years Earlier..."
            "Somewhere in Europe"
            "..."
            e "I don't like this dress..."
            e "I'm a member of the nobility, am I not supposed to look good?"
            scene black
            scene EDress0
            image EDress0 = im.Scale ("EDress0.png", 1920, 1080)
            with fade

            ef "You're too proud little sun... Besides, that dress looks great on you."
            ef "We are powerful and noble indeed, but we should always remember our roots, we are all the same, peasants mages..."
            e "I know... I'm sorry... I was talking without thinking..."
            scene black
            scene EDress1
            image EDress1 = im.Scale ("EDress1.png", 1920, 1080)
            with fade
            e "Remind me father, who owned this before me, one of my old ancestors that I never heard of?"
            ef "In fact, it belonged to your mother."
            e "Wait, Really?"
            ef "Absolutely, she used to wear it quite often."
            ef "She always looked beautiful in it..."
            scene black
            scene Elena
            image Elena = im.Scale ("Elena.png", 1920, 1080)
            with fade
            ef "I remember her smile everytime I see it!"
            ef "(... I also remember what happened when I see it.)"
            ef "(Elena...)"
            e "You always told me how kind and beautiful mother was."
            scene black
            scene EDress3
            image EDress3 = im.Scale ("EDress3.png", 1920, 1080)
            with fade
            e "If she wore it, then I should too."
            e "I'll wear it proudly."
            e "I have to honor her memory."
            ef "..."
            ef "I'm proud of you little sun, come on now we're going to be late..."
            scene black
            e "I'm really curious about those humans!"
            ef "Me too Elise, me too..."
            stop music fadeout 1.0


            "..."
            e "Sooo..."
            e "Let me get this straight..."
            play music "FilledLove.mp3"
            scene black
            scene EQD2
            image EQD2 = im.Scale ("EQD2.png", 1920, 1080)
            with fade
            e "You had a half succubus all along inside of you..."
            m "Yup."
            e "She grew up with your mana."
            m "Yup."
            scene black
            scene LQD2
            image LQD2 = im.Scale ("LQD2.png", 1920, 1080)
            with fade
            e "And... she appeared at night?"
            m "Yah."
            e "That's... odd, to say the least."
            m "(It's odd indeed, were the voices I heard before Lou?)"
            m "(I should ask her when the opportunity arises.)"
            scene black
            scene VLE
            image VLE = im.Scale ("VLE.png", 1920, 1080)
            with fade
            v "Damn, ... This is quite impressive, Humans, learning magic."
            v "I don't know If I will ever be able to master anything."
            l "I mean who cares?"
            scene black
            scene LRV
            image LRV = im.Scale ("LRV.png", 1920, 1080)
            with fade
            l "You're learning for yourself, no one asks you to achieve something special."
            l "You're your own judge."
            scene black
            scene VEA
            image VEA = im.Scale ("VEA.png", 1920, 1080)
            with fade
            e "She's right, besides, you seem perfectly capable."
            v "Well..I-I.."
            h "I agree with them."
            e "Hm ?"
            scene black
            scene HVR
            image HVR = im.Scale ("HRV.png", 1920, 1080)
            with fade
            h "The essence of magic doesn't belong to anyone, anyone should be able to use it freely."
            h "Beside a good friend of mine which is a human did master a few spells quite easily, so I wouldn't be worried!"
            v "Thanks... that might sound a bit rude, but I don't know your name?"
            h "Himia, you can just call me Himia."
            scene black
            scene EHTalk
            image EHTalk = im.Scale ("EHTalk.png", 1920, 1080)
            with fade
            e "Oh, I recognize those white hair you're from the Northern tribes!"
            h "Indeed, and by your red hair, and your freckles I'm guessing you're from the Ancient tribe."
            e "I am! I spent most of my time, near France after the war, I mean, it was the closest to our territory."
            v "... Do you understand anything they're talking about [name]?"
            m "... Not a bit."
            l "Probably elvish curses."
            scene black
            scene EAFire
            image EAFire = im.Scale ("EAFire.png", 1920, 1080)
            with fade

            e "Say [name]!"
            e "I'm curious..."
            e "Can you light one of your fingers using mana?"
            m "Excuse me, what?"
            scene black
            scene ElitF
            image ElitF = im.Scale ("ElitF.png", 1920, 1080)
            e "It's a basic spell, you simply need to sense the mana near your fingers, and light it!"
            e "It's quite useful, when you need some light."
            scene black
            scene VFingerLit
            image VFingerLit = im.Scale ("VFingerLit.png", 1920, 1080)
            v "Wow..."
            m "Sure but... how do I sense mana?"
            e "Oh right, you never learned, don't worry it's really simple!"
            stop music fadeout 1.0
            e "Close your eyes."
            scene black
            play music "rain.mp3"
            e "Focus on the noise around you, the heat of the room..."
            v "This feels like a scuffed asian movie scene..."
            l "I know right, some stuff from those chinese cart-."
            with vpunch
            e "Shh !"
            "You seem in harmony with the room, you cannot hear anything, as if you fainted..."
            "And yet you're still awake, it feels so... calm..."
            e "Can you sense it..?"
            e "Can you feel it ?"
            e "Now think about something."
            e "Feelings love, anger, joy etc..."
            e "They're our way to communicate."
            e "Now focus on your hand and light it!"
            jump spell1

        label spell1:

            menu :

                "Lust":
                    "You open your eyes and check your finger"
                    scene black
                    scene LustFlame
                    image LustFlame = im.Scale ("LustFlame.png", 1920, 1080)
                    with fade
                    e "You did it!"
                    v "Wow !"
                    h "Not bad!"
                    l "That spell might prove useful"
                    e "The flame is hot, and wild and yet welcoming."
                    e "I wonder what kind of emotion you put in that spell."
                    jump cours

                "Might":
                    "you open your eyes and check your finger"
                    scene black
                    scene MightFlame
                    image MightFlame = im.Scale ("MightFlame.png", 1920, 1080)
                    with fade
                    e "You did it!"
                    v "Wow !"
                    h "Not bad!"
                    l "That spell might prove useful"
                    e "The flame burns bright"
                    e "I wonder what kind of emotion you put in that spell."
                    jump cours



                "Love":
                    "You open your eyes and check your finger"
                    if ELove >= 8 and CLove >= 4:
                        scene black
                        scene ECFlame
                        image ECFlame = im.Scale ("ECFlame.png", 1920, 1080)
                        with fade
                        e "You did it!"
                        v "Wow !"
                        h "Not bad!"
                        l "That spell might prove useful"
                        e "Oh, two flames and yet they seem like one... orange with green shadows that's... intriguing"
                        jump cours
                    elif CLove >= 6:
                        scene black
                        scene CFlame
                        image CFlame = im.Scale ("CFlame.png", 1920, 1080)
                        with fade
                        e "You did it!"
                        v "Wow !"
                        h "Not bad!"
                        l "That spell might prove useful"
                        e "Oh the flame turned green, with nice darker reflects, how intriguing"
                        jump cours
                    elif ELove >= 8:
                        scene black
                        scene EFlame
                        image EFlame = im.Scale ("EFlame.png", 1920, 1080)
                        with fade
                        e "You did it!"
                        v "Wow !"
                        h "Not bad!"
                        l "That spell might prove useful"
                        e "The flame has a nice... orange touch, it's... nice."
                        jump cours
                    else:
                        scene black
                        scene FFlame
                        image FFlame = im.Scale ("FFlame.png", 1920, 1080)
                        with fade
                        e "Oh well, seems like you can't light it, don't worry I still felt the changement in the room, try again"
                        e "Maybe... think about something else!"
                        jump spell1

                "Anger":
                    "You open your eyes and check your finger"
                    scene black
                    scene FAnger
                    image FAnger = im.Scale ("FAnger.png", 1920, 1080)
                    with fade
                    e "You did it!"
                    v "Wow !"
                    h "Not bad!"
                    l "That spell might prove useful"
                    e "The flame burns bright, it's huge and menacing, you must be hidding strong feelings behind that one [name]..."
                    jump cours



        label cours:
            scene black
            stop music fadeout 1.0
            "The class finally begins, however, where you expected to learn magic."
            "It ends up being a simple English class."
            "The hour is slow but it finally passes."
            play music "FilledLove.mp3"

            scene Vdoubt
            image Vdoubt = im.Scale ("Vdoubt.png", 1920, 1080)
            with fade
            v "How disapointing, I expected to learn some stuff about Mana, not to ... speak something I've been speaking for years."
            v "And we only have class in the morning, how can we learn anything if we study that little and if we don't even touch any spells?"
            e "It's weird, I too was expecting that..."
            e "I guess we'll have to wait for now and see what else is planned for us this year."
            scene black
            scene Edoubt
            image Edoubt = im.Scale ("Edoubt.png", 1920, 1080)
            with fade
            e "I'll relax on the roof for now."
            v "Well, I need some fresh air too..."
            scene black
            scene MCVL
            image MCVL = im.Scale ("MCVL.png", 1920, 1080)
            with fade
            l "I'll go with you Vanessa."
            menu :
                "Well I'll..."
                "Look for Chumee":
                    m "Hmm, I'll look for Chumee, I haven't seen her today."
                    scene black
                    scene Echoice
                    image Echoice = im.Scale ("Echoice.png", 1920, 1080)
                    with fade
                    e "Oh, she might be near the gymnasium, she's always around there!"
                    scene black
                    jump ChumeeDay3
                "Go with Elise":
                    $ELove += 1
                    scene black
                    scene Echoice
                    image Echoice = im.Scale ("Echoice.png", 1920, 1080)
                    with fade
                    m "I'll go with Elise."
                    e "Sure, I can always use some company!"
                    jump EliseDay3
                "Follow Vanessa and Lou":
                    $VLove += 1
                    $LLove += 1
                    m "I'll go with you."
                    scene black
                    scene Lannoyed
                    image Lannoyed = im.Scale ("Lannoyed.png", 1920, 1080)
                    with fade
                    l "Oh goodie, your questions will ruin the beautiful outside."
                    m "I never mentioned questioning you."
                    scene black
                    scene Lok
                    image Lok = im.Scale ("Lok.png", 1920, 1080)
                    with fade
                    l "Perfect then!"
                    jump VLDay3

            label EliseDay3:
                if ELove >= 9:
                    scene black
                    scene ETRoof
                    image ETRoof = im.Scale ("ETRoof.png", 1920, 1080)
                    with fade

                    e "..."
                    e "I-I've been thinking [name]..."
                    scene black
                    scene ET2Roof
                    image ET2Roof = im.Scale ("ET2Roof.png", 1920, 1080)
                    with fade
                    e "You and I... we grew... closer really fast."
                    e "But with Lou's appearance, I'm wondering if it's not due to her influence..."
                    m "What do you mean."
                    e "She's a succubus, half succubus, maybe, but still, maybe I only feel 'that' towards you because she was here all along..."
                    e "I still feel safe and ... nice around you, but isn't it just an Illusion?"

                    menu :

                        "I don't know...":
                            m "I don't really know what to say Elise..."
                            scene black
                            scene Ego
                            image Ego = im.Scale ("Ego.png", 1920, 1080)
                            with fade
                            e "..."
                            e "I-I should go, I need some time... alone..."
                            menu :
                                "Try to stop her":

                                    $ELove += 1
                                    m "Wait!"
                                    scene black
                                    scene Edepart
                                    image Edepart = im.Scale ("Edepart.png", 1920, 1080)
                                    with fade
                                    m "Elise..."
                                    m "Shit."
                                    jump NextPartD3

                                "Let her go":
                                        scene black
                                        scene Edepart
                                        image Edepart = im.Scale ("Edepart.png", 1920, 1080)
                                        with fade
                                        m "..."
                                        jump NextPartD3

                        "It doesn't matter" if ELove >= 9 and VTrustEliseBeach == True:
                            $ELove += 2
                            m "It doesn't matter."
                            e "Of course it does-"
                            scene black
                            scene EliseRG
                            image EliseRG = im.Scale ("EliseRG.png", 1920, 1080)
                            with fade
                            m "I've been enjoying my time with  you, I-I like you, maybe too much for it to be this early."
                            m "But I do, does it really matter if a succubus influenced that?"
                            e "..."
                            e "You're not wrong... Even though it might be true, it doesn't matter I guess."
                            e "We just feel nice with one another..."
                            scene black
                            m "..."
                            m "...!"
                            scene black
                            scene EMCroof
                            image EMCroof = im.Scale ("EMCroof.png", 1920, 1080)
                            with fade
                            e "... I'm glad I've met you."
                            m "Me too."
                            jump NextPartD3

                else:
                    $ELove += 2
                    e "It's a nice day isn't it?"
                    scene black
                    scene EneutralD3
                    image EneutralD3 = im.Scale ("EneutralD3.png", 1920, 1080)
                    with fade
                    m "It is, but I'm worried about the class we just got"
                    e "Don't worry it was probably just something to prepare us... I hope so."
                    e "Either way let's just relax for a moment!"
                    "You spend some time with Elise, she seem to like you a bit more."
                    jump NextPartD3





                label ChumeeDay3:
                    "Following Elise's instructions you get inside the gymnasium."
                    "You meet a familiar yet unfamilliar face near the changing room."
                    scene black
                    scene mhintro
                    image mhintro = im.Scale ("mhintro.png", 1920, 1080)
                    with fade
                    mh "Oh, a human, we don't see a lot of your kind around here."
                    m "Well-"
                    mh "Don't worry, I have nothing against you or your people, but you're not here for that..."
                    mh "You seem to be looking for someone, maybe I can help!"
                    m "I'm looking for Chum-"
                    scene black
                    scene mhoh
                    image mhoh = im.Scale ("mhoh.png", 1920, 1080)
                    with vpunch
                    mh "OH! So you're the human my sister has been talking about."
                    mh "[name], right ?"
                    m "Yeah."
                    mh "Let me guess, you're hitting on her?"
                    m "Uh..."
                    mh "Either way she's showering."

                    scene black
                    scene mhsmug
                    image mhsmug = im.Scale ("mhsmug.png", 1920, 1080)
                    with fade
                    mh "But I'm kind of bored, so if you want I can just look away and let you get in, I know she's alone inside."
                    m "(What kind of sister does that ?!)"
                    menu :

                        "Get in":
                            scene black
                            scene mhchoice
                            image mhchoice = im.Scale ("mhchoice.png", 1920, 1080)
                            with fade

                            mh "Finally some action!"
                            mh "I like you [name], you're a man of the moment!"
                            mh "Have fun, handsome!"

                            jump CShowerD3
                        "Wait for her to get out":
                            scene black
                            scene mhdisap
                            image mhdisap = im.Scale ("mhdisap.png", 1920, 1080)
                            with fade

                            m "I think I'll just wait."
                            mh "What a Disapointement, I expected a guy going straight to the issue and here I see a Gentleman."
                            jump CoutShower



        label CShowerD3:
            scene black
            with fade
            "You enter the showers."
            "Most of the stalls are empty, only one is used."
            "It's obviously Chumee's."
            menu :

                "Peek":
                    $CLove += 1
                    c "..."
                    scene black
                    scene CShower
                    image CShower = im.Scale ("CShower.png", 1920, 1080)
                    with fade
                    c "...!"
                    scene black
                    scene CShower2
                    image CShower2 = im.Scale ("CShower2.png", 1920, 1080)
                    with fade
                    if CLove >= 6:
                        $CLove += 2

                        c "Come on [name], you can at least come here and take care of my back."
                        c "You're not really discreet you know, I might be small but looking up isn't that hard."
                        scene black
                        "You take off your clothes and join Chumee, she feels a bit tense but her skin is oddly soft..."
                        scene black
                        scene Crub
                        image Crub = im.Scale ("Crub.png", 1920, 1080)
                        with fade

                        m "I didn't really expect to kneel to rub your back."
                        c "Well, I do find a human kneeling for me kind of hot."
                        c "Now... I do hope you didn't came here to 'just rub my back'..."
                        scene black
                        "You grab the Goblin's legs putting her against the wall."
                        c "Right... there..."
                        c "Come on now, put it in, I want it!"
                        "..."
                        c "Fuuuuck! You're fucking huge you know that ?!"
                        m "And you're fucking tight!"
                        m "Are you a virgin?"
                        c "..."
                        c "J-Just fuck me."
                        scene vid CD3
                        m "Maybe your body was meant to fit it."
                        c "Maybe you're... right, maybe I was just created to be your... cocksleeve!"
                        c "Either way, you better not finish outside, I want it!"
                        c "Shit! It feels incredible, I can't believe how good it feels!"
                        c "[name], you better not fucking pullout, I want your seed!"
                        c "Fuuuuuuuuuuck! I love it, it's amazing, I can't live without it!"
                        m "(She's so fucking tight, It's unreal...)"
                        c "I-I.. I'm already at my limit!"
                        c "[name], Don't you fucking pullout, you better cream me or I'm never forgiving you!"
                        scene black
                        scene ECumd3
                        image ECumd3 = im.Scale ("ECumd3.png", 1920, 1080)
                        with fade
                        c "FUCK!!!"
                        scene black
                        scene CPostS
                        image CPostS = im.Scale ("CPostS.png", 1920, 1080)
                        with fade

                        c "D-Dude... I-I can't feel my legs..."
                        m "Shit that was amazing..."
                        c "..."
                        c "Come on now stud, I need to shower, especially since you made me even more dirty."
                        c "I'll see you later [name]."
                        scene black
                        with fade
                        c "Oh and by the way... We're definitely doing it again."
                        $CVirginity = True
                        jump NextPartD3

                    else:
                        c "You're not really Discreet [name], looking up is quite easy!"
                        c "You probably expected to peak, but unfortunatly that won't happen ! Come on join the others I'll be there soon!"
                        scene black
                        "With nothing else to do you leave the room"
                        mh "Oh... cold shower, what a shame."
                        mh "You do look good though, her loss!"
                        m "Well, either way it was nice meeting you...?"
                        scene black
                        scene mhMC
                        image mhMC = im.Scale ("mhMC.png", 1920, 1080)
                        with fade
                        mh "Mahamee, Well you can call me Maha."
                        mh "It was nice meeting you too [name], have a great day!"
                        jump NextPartD3




                "Stay put":
                    scene black
                    scene Cshowerd3
                    image Cshowerd3 = im.Scale ("Cshowerd3.png", 1920, 1080)
                    with fade
                    c "Mahamee, is that you?"
                    c "I told you to-"
                    c "Oh... it's you [name]."
                    m "Wait, how did you recognized me."
                    c "You're tall as hell, and you don't have green legs?"
                    if CLove >= 6:
                        $CLove += 2
                        c "Come on [name], you can at least come here and take care of my back."
                        "You take off your clothes and join Chumee..."
                        scene black
                        scene Crub
                        image Crub = im.Scale ("Crub.png", 1920, 1080)
                        with fade
                        m "I didn't really expect to kneel to rub your back."
                        c "Well, I do find a human kneeling in front of me kind of hot."
                        c "Now... I do hope you didn't came here to 'just rub my back'..."
                        scene black
                        "You grab the Goblin's legs putting her against the wall."
                        c "Right... there..."
                        c "Come on now, put it in!"
                        c "Fuuuuck! You're fucking huge you know that ?!"
                        m "And you're fucking tight!"
                        m "Are you a virgin?"
                        c "..."
                        c "J-Just fuck me."
                        scene vid CD3
                        m "Maybe your body was meant to fit it."
                        c "Maybe you're... right, maybe I was just created to be your... cocksleve!"
                        c "Either way, you better not finish outside, I want it!"
                        c "Shit! It feels incredible, I can't believe how good it feels!"
                        c "[name], you better not fucking pullout, I want your seeds!"
                        c "Fuuuuuuuuuuck! I love it, it's amazing, I can't live without it!"
                        m "(She's so fucking thight, It's unreal...)"
                        c "I-I.. I'm already at my limit!"
                        c "[name], Don't you fucking pullout, you better cream me or I'm never forgiving you!"
                        scene black
                        scene ECumd3
                        image ECumd3 = im.Scale ("ECumd3.png", 1920, 1080)
                        with fade
                        c "FUCK!!!"
                        with hpunch
                        scene black
                        scene CPostS
                        image CPostS = im.Scale ("CPostS.png", 1920, 1080)
                        with fade
                        c "D-Dude... I-I can't feel my legs..."
                        m "Shit that was amazing..."
                        c "..."
                        c "Come on now stud, I need to shower, especially since you made me even more dirty."
                        c "I'll see you later [name]."
                        c "Oh and by the way... We're definitely doing it again."
                        $CVirginity = True
                        jump NextPartD3



                    else :
                        c "I'm almost done, you probably expected to have a peek, but I'm gonna have to deny that request."
                        c "Come on get out I'm almost done, I'll join you and the other when I'm done !"
                        scene black
                        "With nothing else to do you leave the room"

                        scene mhdisap
                        image mhdisap = im.Scale ("mhdisap.png", 1920, 1080)
                        with fade
                        mh "Oh... cold shower, what a shame."
                        mh "You do look good though, her loss!"
                        m "Well, either way it was nice meeting you...?"
                        scene black
                        scene mhMC
                        image mhMC = im.Scale ("mhMC.png", 1920, 1080)
                        with fade
                        mh "Mahamee, Well you can call me Maha."
                        mh "It was nice meeting you too [name], have a great day!"
                        jump NextPartD3











        label CoutShower:
            scene black
            "..."
            scene black
            scene CoutShower
            image CoutShower = im.Scale ("CoutShower.png", 1920, 1080)
            with fade
            c "Oh, [name]."
            c "Sorry I didn't expect you to wait for me."
            if CLove >= 6:
                scene black
                scene Cmhtalk
                image Cmhtalk = im.Scale ("Cmhtalk.png", 1920, 1080)
                with fade
                mh "Your boyfriend is quite boring."
                mh "I wouldn't have been that patient If I was him."
                c "Well, he just knows how to behave!"
                mh "Whatever."
                mh "If you want my opinion, he just wants your ass."
                scene black
                scene CPissed
                image CPissed = im.Scale ("CPissed.png", 1920, 1080)
                with vpunch
                c "Well, maybe I want him to have it!"
                mh "Of course you would, you're in the middle of your heat cycle!"
                c "How would you know that ?!"
                mh "Do you think I'm an idiot, I've been through it Sis."
                scene black
                scene CPissedMC
                image CPissedMC = im.Scale ("CPissedMC.png", 1920, 1080)
                with fade
                c "Whatever, come on [name], let's move."
                scene black
                scene CLeavemh
                image CLeavemh = im.Scale ("CLeavemh.png", 1920, 1080)
                with fade
                mh "Come on, don't take it that bad, you know that I'm messing with you!"
                scene black
                scene mhMC
                image mhMC = im.Scale ("mhMC.png", 1920, 1080)
                with fade
                mh "It was nice meeting you [name], maybe you'll learn how to truly behave the next time we meet."
                scene black
                c "Ugh, she can be irritating!"
                c "Anyway, how are you ?"
                " You spend some time with Chumee she seems to like you more"
                $CLove += 1
                jump NextPartD3


            else:
                scene black
                scene Cmhtalk
                image Cmhtalk = im.Scale ("Cmhtalk.png", 1920, 1080)
                with fade
                mh "It seems you're quite popular sis!"
                c "Leave it, Maha', [name] is a good friend."
                mh "Right 'good friend', whatever you say!"
                c "Don't you have any other person to annoy?"
                mh "Not really, today has been quite boring, I thought I could spend my really boring day with my lovely sister!"
                mh "After all you need someone to help you with your hea-"
                scene black
                scene CPissed
                image CPissed = im.Scale ("CPissed.png", 1920, 1080)
                with fade
                c "SHUT UP!"
                with vpunch
                mh "Oh right he doesn't know..."
                scene black
                scene CPissedMC
                image CPissedMC = im.Scale ("CPissedMC.png", 1920, 1080)
                with fade
                c "Whatever, come on [name], let's move."
                scene black
                scene CLeavemh
                image CLeavemh = im.Scale ("CLeavemh.png", 1920, 1080)
                with fade
                mh "Come on, don't take it that bad, you know that I'm messing with you!"
                scene black
                scene mhMC
                image mhMC = im.Scale ("mhMC.png", 1920, 1080)
                with fade
                mh "It was nice meeting you [name]."
                scene black
                c "Anyway, how are you ?"
                " You spend some time with Chumee she seems to like you more"
                $CLove += 2
                jump NextPartD3

    label VLDay3:
        scene black
        v "J-Just go without me, I have to check something in my locker."
        l "Sure."
        "..."
        scene black
        scene LV1
        image LV1 = im.Scale ("LV1.png", 1920, 1080)
        with fade
        l "Hmm, that Vanessa, she looks... disturbed."
        l "I'm guessing she's the shy girl type, but, I feel like there is something a bit more sad behind that."
        menu :

            "I noticed":
                scene black
                scene LV2
                image LV2 = im.Scale ("LV2.png", 1920, 1080)
                with fade
                $LLove += 1
                m "I noticed... It worries me."
                l "As it should, I'm glad you noticed it."
            "Nothing out of the ordinary":
                scene black
                scene LV3
                image LV3 = im.Scale ("LV3.png", 1920, 1080)
                with fade
                l "Well you might put your head out of your ass for a second."
                l "Hmm, I wonder what though."

        scene black
        scene LV4
        image LV4 = im.Scale ("LV4.png", 1920, 1080)
        with fade
        l "But anyway, I owe you some answers."
        m "I thought-"
        l "I know what I said, but I also know that I must respect what I told you yesterday."
        stop music fadeout 1.0
        l "Shoot."
        play music "Blind.mp3"

        jump QD3Lou

    label QD3Lou:


        menu :

            "What power did you talk about?":
                scene black
                scene LV5
                image LV5 = im.Scale ("LV5.png", 1920, 1080)
                with fade
                l "Oh, that 'power' I remember this dream of yours."
                l "I cannot lend you my power, neither 'directly' corrupt."
                l "I feed from the Lust you felt toward the girls you met a few days ago."
                l "My existence does have an important impact on them though."
                l "But It's not corruption I don't break their mind to beg for cocks."
                l "It's at best a push to do what they wanted to, a boost of adrenaline to dare something."
                jump QD3Lou

            "What happened during that war?":
                scene black
                scene LV5
                image LV5 = im.Scale ("LV5.png", 1920, 1080)
                with fade
                l "Hm... The war is a lie, some of us like Elise were able to be lucid enough to see the truth."
                l "Although it's not clear, I feel like my memory has holes."
                m "That's a feeling Elise shared..."
                l "Well, that might be an important clue."
                l "I just remember my father repeating the same phrase."
                l "Everything you know is a lie."
                l "And I definitely intend to find out what's going on and what he meant by that."
                jump QD3Lou


            "How do you feel about being part of our group?":
                scene black
                scene LV6
                image LV6 = im.Scale ("LV6.png", 1920, 1080)
                with fade
                l "It's nice!"
                l "I was worried that I would be rejected, or that the girls would be annoying."
                l "But I feel quite nice with them."
                l "I'm glad you care about my well being."
                jump QD3Lou


            "What's next?":
                scene black
                scene LV5
                image LV5 = im.Scale ("LV5.png", 1920, 1080)
                with fade
                l "Well, I do have to find the meaning of my father's words."
                l "And I'm pretty sure Elise can help us, she's an elf and she seem to be a good person."
                jump QD3Lou


            "Who exactly were your parents?":
                scene black
                scene LV2
                image LV2 = im.Scale ("LV2.png", 1920, 1080)
                with fade
                l "My father was some sort of... Warlock."
                m "A Warlock? Like summoning demons, and carrying soulshards type of warlock?"
                l "I don't know about the Soulshard part, but yeah."
                l "My father was a good man, but he lost faith in human relationship."
                l "He summoned my mother, and well they both fell in love for one another."
                l "My mother gave up her succubus powers and well here I am now."
                scene black
                scene LV7
                image LV7 = im.Scale ("LV7.png", 1920, 1080)
                with fade
                l "..."
                jump QD3Lou

            "What was that dream yesterday?":
                scene black
                scene LV5
                image LV5 = im.Scale ("LV5.png", 1920, 1080)
                with fade
                l "I didn't influence your dream yesterday [name]."
                m "Well I do remember being Elise's father."
                l "Well maybe your mind is trying to tell you something then."
                m "(Weird.)"
                jump QD3Lou


            "Continue":
                jump VLD3Suite

    label VLD3Suite:
        $LLove += 1
        scene black
        v "Sorry, had to change, I feel way better in my casual clothes!"
        l "It's fine."
        scene black
        scene VL8
        image VL8 = im.Scale ("VL8.png", 1920, 1080)
        with fade
        v "What were you two talking about while I was gone?"
        m "Uh-."
        l "Oh, [name] told me how glad he was to have you in his life."
        v "Oh Really ?"
        menu:

            "Yeah":
                $VLove += 1
                $LLove += 1
                m "Well, yeah..."
            "No":
                m "What? N-"
                with hpunch
                l "The poor thing, look at how he's blushing."

        v "That's... nice, thanks [name], I needed that."
        scene VBFlame
        image VBFlame = im.Scale ("VBFlame.png", 1920, 1080)
        with fade
        l "Hey Vanessa!"
        l "How about trying to light your finger!"
        l "Just like Elise showed us this morning!"
        v "I don't know If I could do it..."
        l "Of course you could, and you can."
        l "Just focus, close your eyes do all of that meditation stuff!"
        v "I-I guess I could try."
        scene black
        scene VFocus
        image VFocus = im.Scale ("VFocus.png", 1920, 1080)
        with fade

        menu :
            "I'm sure you can do it!":
                $VLove += 2
                v "Y-you're right, I can do it, I will do it!"
                l "That's the spirit!"
                scene black
                "..."
                if VLove >= 10:
                    v "...!"
                    scene black
                    scene VFlameS
                    image VFlameS = im.Scale ("VFlameS.png", 1920, 1080)
                    with fade
                    v "I MADE IT!"
                    l "Wow You made it!"
                    l "I told you you could!"
                    l "What emotion was behind it!"
                    scene black
                    scene VFeel
                    image VFeel = im.Scale ("VFeel.png", 1920, 1080)
                    with fade
                    v "That..."
                    v "Is a secret."
                    scene black
                else:
                    scene black
                    scene VFlameF
                    image VFlameF = im.Scale ("VFlameF.png", 1920, 1080)
                    with fade
                    v "Shit"
                    v "It burns!"
                    l "Well, the flame did appear, but it's not supposed to be painful."
                    l "What emotion is behind it?"
                    scene black
                    v "It's a secret..."

            "Don't say anything":
                scene black
                "..."
                if VLove >= 10:
                    v "...!"
                    scene black
                    scene VFlameS
                    image VFlameS = im.Scale ("VFlameS.png", 1920, 1080)
                    with fade
                    v "I DID IT!"
                    l "Wow, You made it!"
                    l "I told you you could!"
                    l "What emotion was behind it!"
                    scene black
                    scene VFeel
                    image VFeel = im.Scale ("VFeel.png", 1920, 1080)
                    with fade
                    v "That..."
                    v "Is a secret."
                    scene black
                else:
                    scene black
                    scene VFlameF
                    image VFlameF = im.Scale ("VFlameF.png", 1920, 1080)
                    with fade
                    v "Shit"
                    v "It burns!"
                    l "Well, the flame did appear, but it's not supposed to be painful."
                    l "What emotion is behind it?"
                    scene black
                    v "It's a secret..."

        "The three of you spend some time together, Lou & Vanessa seems to like you more."
        jump NextPartD3

    label NextPartD3:
        stop music fadeout 0.5

        play music "blackbird.mp3"
        scene black
        scene Regroupd3
        image Regroupd3 = im.Scale ("Regroupd3.png", 1920, 1080)
        with fade
        "After a few hours, you all regroup in the courtyard..."
        l "I like how you blend in the grass, Chumee."
        scene black
        scene LCTalk
        image LCTalk = im.Scale ("LCTalk.png", 1920, 1080)
        with fade
        c "What can I say, being a greenskin is amazing!"
        c "And you do blend well with the sunlight!"
        l "Say, why are you not in class with us?"
        c "I don't pay attention to all this 'magic' nonsense"
        c "Magic makes people lazy!"
        scene black
        scene LCtalk3
        image LCtalk3 = im.Scale ("LCtalk3.png", 1920, 1080)
        with fade
        e "That's not true, I am far from Lazy and yet I'm quite the mage."
        c "Whatever, wood elf, what I'm saying is no magic spell replaces performences made using your blood & sweat!"
        scene black
        scene VLLeave
        image VLLeave = im.Scale ("VLLeave.png", 1920, 1080)
        with fade
        c "Anyway, It's getting late, I should get home."
        v "Yeah me too..."
        l "Go ahead Vanessa, I'll join you later, I just have to ask something to [name] and Elise."
        l "In private..."
        v "Uh sure I guess, see you later!"
        stop music fadeout 1.0
        scene black
        scene LE1
        image LE1 = im.Scale ("LE1.png", 1920, 1080)
        with fade
        e "Hm?"
        l "So Elise, you too know the truth?"
        e "What truth?"
        l "'Everything you know is a lie.'"
        play music "mystery.mp3"
        scene black
        scene LE2
        image LE2 = im.Scale ("LE2.png", 1920, 1080)
        with fade
        e "WH-"
        l "Don't worry, I'm on your side."
        e "Wait how do you know the truth, you came to life a day ago!"
        l "I'll tell you, I promise, but I need you to do something for me."
        e "Hmm...What?"
        l "You're an elf, and you look very noble, you probably know more than me."
        l "You and [name] should head to the School's library and find any clue we can get."
        e "Why would any clue be in there?"
        l "Does the name 'Helirios' sounds familiar to you?"
        scene black
        scene LE3
        image LE3 = im.Scale ("LE3.png", 1920, 1080)
        with fade
        e "!!!"
        with vpunch
        e "HOW DO YOU KNOW HIS NAME?!"
        l "As I said, I'll tell you and [name], but not now. I need you both to trust me."
        menu :

            "Trust Lou":
                $LLove += 1
                l "Thank you [name]..."
                l "Elise?"
                scene black
                scene LE4
                image LE4 = im.Scale ("LE4.png", 1920, 1080)
                with fade
                e "... Fine, if you knew my father's name, you must know enough for me to trust you."
                l "Thanks! You won't regret it!"
                l "Find a book written by this author."
                l "You might find... interesting clues."
                l "I do not know much about him, but my mother did."
                scene black
                scene LE6
                image LE6 = im.Scale ("LE6.png", 1920, 1080)
                with fade
                e "Your mother?"
                e "...hmm..."
                e "Let's go [name]."
                jump Libraryd3
            "Doubt":
                l "*Sigh*"
                l "I understand, but for now we have nothing better to do."
                l "Find a book written by this author."
                scene black
                scene LE5
                image LE5 = im.Scale ("LE5.png", 1920, 1080)
                with fade
                l "You might find... interesting clues."
                l "I don't know much about him, but my mother did."
                scene black
                scene LE6
                image LE6 = im.Scale ("LE6.png", 1920, 1080)
                with fade
                e "Your mother?"
                e "...hmm..."
                e "Let's go [name]."
                jump Libraryd3

    label Libraryd3:
        stop music fadeout 1.0
        scene black
        scene EL1
        image EL1 = im.Scale ("EL1.png", 1920, 1080)
        with fade
        e "Hmm..."
        m "Still doubting?"
        e "Yeah..."
        e "Helirios, my father..."
        play music "blackbird.mp3"
        scene black
        scene EL2
        image EL2 = im.Scale ("EL2.png", 1920, 1080)
        with fade
        m "How was he ?"
        e "Oh, I think you would've liked him."
        e "Discreet, kind, smart, maybe a bit silly."
        m "Sounds like a great man."
        scene black
        scene EL3
        image EL3 = im.Scale ("EL3.png", 1920, 1080)
        with fade
        e "He was... And I miss him."
        menu:

                "Well, now you have me!" if ELove >= 10:
                    $ELove += 2
                    scene black
                    scene EL4
                    image EL4 = im.Scale ("EL4.png", 1920, 1080)
                    with fade
                    e "And you have me!"
                    m "And I don't need anything else."
                    scene black
                    scene EL5
                    image EL5 = im.Scale ("EL5.png", 1920, 1080)
                    with fade
                    e "Oh...T-That was sweet."
                    e "C-Come on, let's look for those books [name]."

                "He would be proud":
                    $ELove += 1
                    e "I don't know..."
                    m "Come on, you know I'm right!"
                    m "Now Cheer up pointy ears, we have answers to look for!"
                    scene black
                    scene EL6
                    image EL6 = im.Scale ("EL6.png", 1920, 1080)
                    with fade
                    e "Haha, you're right Ape hands... Thanks."

        scene black
        "You finally enter the Library."
        "It's traditional."
        "Like any Library, stalls filled with books, some tables and chairs."
        "Nothing extraordinary."
        scene black
        scene EL7
        image EL7 = im.Scale ("EL7.png", 1920, 1080)
        with fade
        e "This looks a bit empty, it's making me miss the great Library of my Father."
        m "Your father had a Library?"
        scene black
        scene EL8
        image EL8 = im.Scale ("EL8.png", 1920, 1080)
        with fade
        e "Yeah! Full of books, stories, spells!"
        e "I still have a few books mysel-."
        h "Oh, hey!"
        scene black
        scene EL11
        image EL11 = im.Scale ("EL11.png", 1920, 1080)
        with fade
        e "Himia? Hi, what are you doing here this late?"
        h "I often like to come here and read some stories, I could spend the night here!"
        h "And you two, what are you doing... Alone, at this time, I don't mind hearing you guys make out as long as you're not in front of m-"
        scene black
        scene EL9
        image EL9 = im.Scale ("EL9.png", 1920, 1080)
        with fade
        with vpunch
        e "N-N-NO!"
        if ELove >= 12:
            m "Awh..."
            scene black
            scene EL10
            image EL10 = im.Scale ("EL10.png", 1920, 1080)
            with fade
            e "{size=-10} Maybe later... {/size}"
            scene black
            scene EL11
            image EL11 = im.Scale ("EL11.png", 1920, 1080)
            with fade
            e "For now, we're looking for a books, from Helirios"
        else:
            scene black
            scene EL11
            image EL11 = im.Scale ("EL11.png", 1920, 1080)
            with fade
            m "We're looking for books from Helirios."

        h "Oh, the famous Helirios, I love his books!"
        stop music fadeout 1.0
        h "A shame he ended up being a traitor..."
        with hpunch
        scene black
        scene EL9
        image EL9 = im.Scale ("EL9.png", 1920, 1080)
        with fade
        e "A-A Traitor?!"
        play music "Mystery2.mp3"
        e "What... are you talking about?"
        h "You do know that he is the one that started the war?"
        e "...!"
        e "Wha-."
        scene black
        scene EL12
        image EL12 = im.Scale ("EL12.png", 1920, 1080)
        with fade
        m "Elise?"
        e "I-It's fine."
        e "I need some time alone [name]."
        h "Are you alright?"
        e "Yeah don't worry."
        h "Say [name], mind sitting with me for a moment, I'm really curious about you!"
        m "Suuure..."
        scene black
        scene EL13
        image EL13 = im.Scale ("EL13.png", 1920, 1080)
        with fade
        h "So!"
        h "I will ask you a few questions about you and your people."
        h "And in return, I'll answer yours!"
        h "Sounds good?"
        m "Yeah."
        h "Great so..."
        h "A bit of a personal question, but do you have any favorite Literary movement?"
        m "(That's quite the bookworm question.)"
        menu :

            "Naturalism":
                $HLove += 1
                scene black
                scene EL14
                image EL14 = im.Scale ("EL14.png", 1920, 1080)
                with fade
                h "Oh, naturalism, that's an interesting choice."
                h "I did read a few books about it, what an interesting movement."
                h "Painting science & nature over words."
                m "(Guess I'm getting a class now.)"
                m "Say you're quite the bookworm!"
                h "Yeah... Sorry I just love diving in a book, so many stories, facts..."

            "Romanticism":
                $HLove += 1
                scene black
                scene EL14
                image EL14 = im.Scale ("EL14.png", 1920, 1080)
                with fade
                h "Ah, it's a classic, but it's great."
                h "... Each pages are white until you color them using pretty words."
                h "Knowledge & happiness"
                h "So many ways to write Love, sadness, happiness on a piece of paper!"
                m "(Guess I'm getting a class now.)"
                m "Say you're quite the bookworm!"
                h "Yeah... Sorry I just love diving in a book, so many stories, facts..."

            "Realism":
                $HLove += 1
                scene black
                scene EL14
                image EL14 = im.Scale ("EL14.png", 1920, 1080)
                with fade
                h "Oh, that's surprising, but I guess that's fitting."
                h "Not seeing a page white, nor black, nor colorful."
                h "Just seeing a page."
                h "The Brutal truth!"
                m "(Guess I'm getting a class now.)"
                m "Say you're quite the bookworm!"
                h "Yeah... Sorry I just love diving in a book, so many stories, facts..."

        scene black
        scene EL15
        image EL15 = im.Scale ("EL15.png", 1920, 1080)
        with fade
        h "Say, humans were reduced to slavery for 30 years."
        h "How were you able to learn that style, you're merely 20."

        m "Cities were a bad place to be, I've been raised by Vanessa's mother, she was a great reader as well."
        m "Taught me and Vanessa great authors, we would always join her near the fireplace where she would read us a story when we were younger."
        m "Then I started reading myself, anything was better than the TV during that period."
        scene black
        scene EL16
        image EL16 = im.Scale ("EL16.png", 1920, 1080)
        with fade
        h "...O-Oh... I see."
        h "She must be an amazing person that woman."
        m "She was."

        m "Anyway, let's move forward, the past is behind!"
        scene black
        scene EL14
        image EL14 = im.Scale ("EL14.png", 1920, 1080)
        with fade
        h "Indeed!"
        h "Soooooo... I've read these, japanese Comics and Discovered that 'Anime Culture', are those inspired by fact or are they the fruit of imagination?"

        menu :

            "They're not real":
                scene black
                scene EL16
                image EL16 = im.Scale ("EL16.png", 1920, 1080)
                with fade
                h "Oh... that's a shame."
                h "But I guess it doesn't matter, a story is a story!"

            "Some are inspired of real stories":
                scene black
                scene EL14
                image EL14 = im.Scale ("EL14.png", 1920, 1080)
                with fade
                h "Oh, that's interesting, some are stories others are real."
                h "I wonder which are true, and which are fiction!"

            "Anime was a mistake.":
                scene black
                scene EL13
                image EL13 = im.Scale ("EL13.png", 1920, 1080)
                with fade
                h "Except Jojo's bizarre adventure I hope!"
                h "It's my favorite!"
                m "(She has good taste.)"

        h "Anyway, You answered my questions, time for me to answer yours!"

    label QHimia:

        menu :

            "Where do you come from?":
                $HLove += 1
                scene black
                scene EL14
                image EL14 = im.Scale ("EL14.png", 1920, 1080)
                with fade
                h "I come from the northern elven tribe."
                h "As you know Elves lived on small Island hidden by the mist for ages."
                h "Elise comes from the Ancient tribe, an island near Europe close to France."
                h "While I lived on a small Island between Greenland and Iceland."
                jump QHimia

            "What's the deal with your brother?":
                scene black
                scene EL16
                image EL16 = im.Scale ("EL16.png", 1920, 1080)
                with fade
                h "Oh... I know, he doesn't feel the same way as I toward humans."
                h "My brother sort of had, traumatics experiences with humans..."
                h "I'll tell you one day... I don't feel ready to talk about it right now..."
                jump QHimia

            "You don't feel any kind of hatred toward mankind?":
                scene black
                scene EL13
                image EL13 = im.Scale ("EL13.png", 1920, 1080)
                with fade
                h "Not a bit, I judge a person on it's actions."
                h "A lot of humans did terrible things in the past but a lot also did amazing stuff!"
                jump QHimia

            "What do you think of human literature?":
                $HLove += 1
                scene black
                scene EL13
                image EL13 = im.Scale ("EL13.png", 1920, 1080)
                with fade
                h "It's really interesting, all those bits of stories are incredible."
                h "And I find your history quite invegorating, War is terrible but it's part of your legacy."
                h "Hatred, love, for peace or to prove anything."
                h "We elves too waged war by the past, Maybe war is for everyone afterall."
                jump QHimia

            "How were you able to communicate through the mist?":
                scene black
                scene EL13
                image EL13 = im.Scale ("EL13.png", 1920, 1080)
                with fade
                h "Portals, even though we were all isolated, every tribe were able to communicate with each others."
                jump QHimia

            "Continue":
                jump LibraryPart2

    label LibraryPart2:
        scene black
        scene EL13
        image EL13 = im.Scale ("EL13.png", 1920, 1080)
        with fade
        h "That was nice, but I should get going, it's getting late."
        h "You should check on Elise."
        h "It was great meeting you [name]!"
        scene black
        "You wave back at Himia and join Elise, near the back of the room."
        e "... A traitor."
        scene black
        scene EL19
        image EL19 = im.Scale ("EL19.png", 1920, 1080)
        with fade
        e "Everybody thinks my father is a traitor."
        e "Even his memory is forgotten."
        if ELove >= 12:
            $ELove += 2
            m "..."
            scene black
            scene EL17
            image EL17 = im.Scale ("EL17.png", 1920, 1080)
            with fade
            e "...?"
            with vpunch
            scene black
            scene EL18
            image EL18 = im.Scale ("EL18.png", 1920, 1080)
            with fade
            "You can feel, her hair, warmed by the light of the sun."
            "You keep feeling her hair until her gaze meet yours."
            e "..."
            scene black
            scene EL20
            image EL20 = im.Scale ("EL20.png", 1920, 1080)
            with fade
            e "C-Can you keep your hand against me?"
            e "I-It's warm...Reassuring..."
            scene black
            scene EL21
            image EL21 = im.Scale ("EL21.png", 1920, 1080)
            with fade
            m "Of course..."
            scene black
            scene EL22
            image EL22 = im.Scale ("EL22.png", 1920, 1080)
            with fade
            e "It's so nice... There is no noise, nothing to disturb us, just you and me."
            e "... Careful, my ears are sensitive."
            m "That's good to know..."
            scene black
            scene EL23
            image EL23 = im.Scale ("EL23.png", 1920, 1080)
            with fade
            e "I'm sure it is..."
            e "... Come on we should look for those books."
            m "Yeah."
            stop music fadeout 1.0
            jump LibraryPart3


        else:
            $ELove += 1
            scene black
            scene EL24
            image EL24 = im.Scale ("EL24.png", 1920, 1080)
            with fade
            m "I'm sorry Elise, but the best thing we can do for now..."
            m "Is find out the truth, and clean your father's memory."
            e "..."
            e "You're right."
            e "... Come on we shoud look for those books."
            m "Yeah."
            stop music fadeout 1.0
            jump LibraryPart3

        label LibraryPart3:
                scene black

                "You spend a few minutes with Elise looking for any books."
                scene black
                scene EL25
                image EL25 = im.Scale ("EL25.png", 1920, 1080)
                with fade
                e "... Nothing."
                e "Why would a School promote the books of a traitor anyway."
                m "Your father, he was a great mage right?"
                e "Absolutely, he was a great Magister for my people."
                m "Hmm... What if you used your mana to look for it?"
                e "My mana? Why?"
                m "Think about it!"
                m "Maybe he left a hint for you, you're his daughter after all!"
                play music "rain.mp3"

                e "Hmm, you're right."
                e "Let me give it a shot."
                scene black
                scene EL26
                image EL26 = im.Scale ("EL26.png", 1920, 1080)
                with fade
                "The room takes a cosy, nightlike feeling."
                "..."
                "...!"
                m "Elise, that Book, it's standing out from the others!"
                m "A Japanese Dictionary?"
                scene black
                "You grab the book, and put it on a table."
                "The book opens itself, the covers change, you notice the title of the book floating in the air."
                scene black
                scene EL27
                image EL27 = im.Scale ("EL27.png", 1920, 1080)
                with fade
                e "Hm... 'Le Conte de L'unité.'"
                m "Excuse me, what?"
                scene black
                scene EL28
                image EL28 = im.Scale ("EL28.png", 1920, 1080)
                with fade
                e "It's written... 'Le conte de l'unité.'"
                e "It would make sense, since you know we were quite close to France during the first years."
                m "The first years?"
                e "Yeah the first years, when we met humans for the fi-"
                e "Wait..."
                scene black
                scene EL29
                image EL29 = im.Scale ("EL29.png", 1920, 1080)
                with fade
                e "I'M REMEMBERING IT!"
                e "Lilian, was the first human I met with my father!"
                e "And... Ugh, I still have trouble remembering it!"
                e "That book is indeed a key!"
                scene black
                scene EL28
                image EL28 = im.Scale ("EL28.png", 1920, 1080)
                with fade
                m "Well that's amazing, but I'm not reading your french gibberish."
                e "Then what are you reading?"
                m "Tales of Unity."
                e "Oh, then it's not written in French."
                e "My father used 'mental runes' to write, Runes that takes form in letters and words that the reader understands."
                m "Wait so you're french?"
                scene black
                scene EL30
                image EL30 = im.Scale ("EL30.png", 1920, 1080)
                with fade
                e "Well, I guess, I mean I do hope you know I'm a fancy lady [name]!"
                e "I'm from the Ancient tribe, though I guess you could refer to me as a Wood elf jokes aside."
                e "Either way, that book is a great discovery!"
                e "Oh Father, what would I be without you!"
                e "Let's get to my place [name], we'll have time to decipher everything there."
                scene black
                "Elise grabs the book close to her chest, and you both depart for her place."
                "..."
                "Meanwhile at your place."
                scene black
                scene VL1
                image VL1 = im.Scale ("VL1.png", 1920, 1080)
                with fade
                l "You look devastated."
                v "Well I've been feeling that way for a few days now..."
                v "Since you met Elise and Chumee, right?"
                v "... [name] seems to feel way better with them."
                v "They're smart, beautiful, kind, who am I to compete?"
                l "You're yourself, there is only one Vanessa in the world like you."
                l "You're just as good as they are."
                l "[name] seems to care about you."
                v "Oh, I don't know, I don't want him to worry about me, but... Thanks."
                scene black
                scene VL7
                image VL7 = im.Scale ("VL7.png", 1920, 1080)
                with fade
                l "Sorry, but thanks won't be enough to prove to me you feel alright."
                l "And I feel like I can take care of you right now."
                scene black
                l "Vanessa, will you allow me to please you?"
                v "A-Are you using your powers?"
                l "I don't want to corrupt you, you love someone else."
                l "I just want you to feel confident, and to do it."
                v "... Yes, I want you to please me."
                scene vid E
                l "..."
                v "(It feels amazing!)"
                v "(And yet I feel like I can't control my body...)"
                v "Fuck... that's good..."
                l "You're quite tasty yourself..."
                v "..."
                scene vid F
                v "FUCK!"
                with hpunch
                v "That's great!"
                v "Nice... and slow..."
                v "Just what I needed..."
                v "I love your tongue..."
                "..."
                v "S-shit I think I'm cu..-cu.."
                scene black
                scene VL9
                image VL9 = im.Scale ("VL9.png", 1920, 1080)
                with fade
                v "CUMMING!"
                with hpunch
                l "That's it, just let it go, focus on the pleasure..."
                v "I loved it..."
                v "I feel relieved..."



                stop music fadeout 1.0



                scene black
                scene VL2
                image VL2 = im.Scale ("VL2.png", 1920, 1080)
                with fade
                v "..."
                play music "TiredOfLife.mp3"
                v "Thanks...For taking care of me."
                l "Don't thank me, now we're family."
                l "And I don't want my 'older sister' to feel sad or to carry too much on her shoulders."
                v "...That sounds really weird now."
                l "Yeeaaaah, but I mean there is no blood connecting us so... Do we really care?"
                v "You're right."
                l "..."
                scene black
                scene VL3
                image VL3 = im.Scale ("VL3.png", 1920, 1080)
                with fade
                l "[name]... You love him, don't you?"
                v "I-I do."
                v "But... I never had the courage to do anything."
                l "You're a great person Vanessa, I'm sure of it, but you need to get yourself together."
                l "You're as important to him as anyone else, you're important to me too, even though we've known each other for a day at most."
                v "You're right."
                v "I need to act."
                scene black
                scene VL4
                image VL4 = im.Scale ("VL4.png", 1920, 1080)
                with fade
                l "That's the spirit!"
                v "And... you?"
                v "Any plans? For your future I mean."
                scene black
                scene VL5
                image VL5 = im.Scale ("VL5.png", 1920, 1080)
                with fade
                l "Oh... I-I'm not sure yet."
                l "For now... I'm just glad to be alive and to have you two."
                l "I feel like my family is back, my caring and loving mother."
                l "And my silly father."
                l "It feels, peaceful, but I feel like this peace might be disturbed soon, it's sort of a feeling..."
                v "Hmm, that's worrying... but I guess there isn't much we can do for now."
                v "I'm curious about what happened to you in the past."
                l "Me too."
                l "..."
                scene black
                scene VL2
                image VL2 = im.Scale ("VL2.png", 1920, 1080)
                with fade
                v "... We should get some sleep I'm a bit tired."
                l "Yeah, after what I did I feel like I could use some rest too!"
                l "You know I can't refuse the taste of a sweet woman like you!"
                l "It's in my blood... Literally."
                scene black
                scene VL6
                image VL6 = im.Scale ("VL6.png", 1920, 1080)
                with fade
                v "Well maybe we'll be able to do it again..."
                l "Or maybe [name] will join us this time."
                v "W-W-Well M-Maybe."
                scene black
                l "Come on, sweet dreams Vanessa."
                v "You too Lou."

                if CLove >= 8 and CVirginity == True:
                    mh "Oh it's so sweet!"
                    mh "My sis finally has a crush on someone!"
                    scene black
                    scene CM1
                    image CM1 = im.Scale ("CM1.png", 1920, 1080)
                    with fade
                    c "Shut up Maha, you know it's just to get rid of that heat bullshit!"
                    mh "Oh don't you lie to me now."
                    mh "You enjoyed every seconds of it, and I'm sure you prefered the fact that he was the one doing it more than just having something stuffed in your vagina."
                    c "You're fucking annoying, it's not LOVE!"
                    with vpunch
                    mh "Come on don't shout at me!"
                    mh "It's not a bad thing at all, falling in love, having a family, it's so sweet!"
                    scene black
                    scene CM2
                    image CM2 = im.Scale ("CM2.png", 1920, 1080)
                    with fade
                    c "I-I don't want to have childrens! It's too early!"
                    mh "Not now of course, but come on, you're a growing Goblin, or should I say, a stretching one."
                    c "N-Nothing's been stretched! He's just a fuck buddy at best!"
                    scene black
                    scene CM3
                    image CM3 = im.Scale ("CM1.png", 1920, 1080)
                    with fade
                    dai "Well, he did pop your cherry."
                    scene black
                    scene CM4
                    image CM4 = im.Scale ("CM4.png", 1920, 1080)
                    with fade
                    c "Shut up Dai!"
                    mh "Oh, I forgot you could talk."
                    dai "Well I don't often agree with Maha, but she's right, even if you're in heat."
                    dai "It's still your virginity."
                    c "Don't say it like that! It's weird coming from you."
                    scene black
                    scene CM5
                    image CM5 = im.Scale ("CM5.png", 1920, 1080)
                    with fade

                    mh "I'll let you in denial Sis."
                    mh "But there is nothing wrong about loving someone."
                    scene black
                    scene CM6
                    image CM6 = im.Scale ("CM6.png", 1920, 1080)
                    with fade
                    c "..."
                    c "Mh..."
                    jump ElisePlace

                else:
                    jump ElisePlace


    label ElisePlace:
        scene black
        "After a long walk with Elise, you finally get to her place."
        "It's a simplistic student apartment, nothing that would stand out of the ordinary."
        e "Here let me turn on the light, and let's get into it!"

        scene black
        scene EB1
        image EB1 = im.Scale ("EB1.png", 1920, 1080)
        with fade
        e "Sooo... The book seem to contain spells."
        e "And messages from the past, although most of the pages are absolutely empty!"
        scene black
        scene EB2
        image EB2 = im.Scale ("EB2.png", 1920, 1080)
        with fade
        e "There is one page though, the first one."
        e "Avdødes gave."
        m "Bless you."
        scene black
        scene EB1
        image EB1 = im.Scale ("EB1.png", 1920, 1080)
        with fade
        e "No, I mean 'Avdødes gave', it's the name of the spell of the first page."
        m "Why is it not translated."
        e "Well, maybe that was written by someone else than my father, someone that spoke Norwegian."
        scene black
        scene EB2
        image EB2 = im.Scale ("EB2.png", 1920, 1080)
        with fade
        e "Let me read the description."
        e "'Whom knows his past, accept the truth.'"
        m "What does that mean?"
        scene black
        scene EB3
        image EB3 = im.Scale ("EB3.png", 1920, 1080)
        with fade
        e "I have no idea, although there are some spells instruction."
        e "Let's try to use that spell [name]."
        m "Alright, what am I supposed to do?"
        e "Just read the incantation, it's norwegian as well."
        m "But I don't speak norwegian."
        scene black
        scene EB1
        image EB1 = im.Scale ("EB1.png", 1920, 1080)
        with fade
        e "Languages are but a way for people to communicate, you can speak it using magic."
        e "Trust me and read as best as you can you'll see!"
        scene black
        "You both close your eyes and repeat the same sentence at an exact timing."
        "Meg fra den nåværende tidslinjen, dvel i sannheten som er min."
        "The sentence sings like a sweet melody in your ear, clear as crystal, cold as the north."
        "You feel your soul leaving your body."
        "..."
        jump Book

    label Book:
            scene black
            scene ToUBook
            image ToUBook = im.Scale ("ToUBook.jpg", 1920, 1080)
            with fade

            menu :

                    "The white haired mage.":
                        $TaleWhiteMage = True
                        scene black
                        ef "I am Helirios."
                        ef "And if you're reliving this memory, it means my plan to preserve the truth succeeded."
                        e "... Father?"
                        "You seem to hear Elise's voice alongside Helirios'"
                        "Everything is yet dark, there are no lights, although you feel Elise's comforting presence, and before being able to say anything else..."
                        "The mage returns to his monologue."
                        ef "***** Seems to be trying to manipulate the memories of everyone, the mad fool!"
                        m "W-what, the beginning of his sentence was impossible to understand."
                        ef "I don't know in what kind of world I am speaking to."
                        ef "But know that 'Everything is a lie'"
                        ef "Either way, maybe my past will allow you to fight my battle, for I am probably dead."
                        "..."
                        scene black
                        scene HL
                        image HL = im.Scale ("HL.png", 1920, 1080)
                        with fade
                        ef "To fight the Armaggedon, I needed an ally."
                        ef "And I got one."
                        ef "Me, Magister of my people."
                        ef "And Lilian, even though her origins are still a bit blurry for me."
                        ef "I could always count on her, I always had her back and she always had mine."
                        jump Book
                    "The red widow." if TaleWhiteMage == True:
                        $TaleRedWidow = True
                        lm "Ah, the sweet kiss of the sun."
                        lm "I missed it, if only Helirios could look beyond his dusty books he could see how beautiful this world is!"
                        lm "'We have to study ways to preserve the world if you want to see it Lilian, think about your child's future!'"
                        lm "Yeah, that's what he would say."
                        lm "But I can't blame him."
                        lm "And... as a father, he's not wrong."
                        lm "I just hope wherever he is, ***** is safe..."
                        "Lilian's memories seems shattered, that one lacks a visual support."

                        jump Book
                    "Instructions":
                        "While casting 'Avdødes gave' You've been sent through the memories of past heroes."
                        "Everytime you encounter this screen you are able to visit the past."
                        "Depending of your choices more paths & memories will unlock."
                        "You can access the Grimoire once every day at night depending on the current event of the game."
                        jump Book

                    "Continue":
                        jump EliseTwist


    label EliseTwist:
        scene black
        scene EB4
        image EB4 = im.Scale ("EB4.png", 1920, 1080)
        with fade
        e "That... That was weird."
        m "Yeah..."
        scene black
        scene EB5
        image EB5 = im.Scale ("EB5.png", 1920, 1080)
        with fade
        e "It seems like this spell allowed us to read messages from the past."
        e "And it seems like... those tales... The White haired mage..."
        e "The Red Widow..."
        e "I remember now, Helirios my father teamed up with Lilian, the red widow."
        e "It's coming along, Lilian being Pregnant, and a bit silly and warm beneath her ...'Open' ways."
        e "I was able to remember the past, but I there are still things to be remembered."
        scene black
        scene EB6
        image EB6 = im.Scale ("EB6.png", 1920, 1080)
        with fade
        e "Hm... at first this book had 1 page, with the spell."
        e "But now it seems like it has more pages, pages that summarizes the tale we relived."
        e "But... wait there is another one that is now filled up too."
        e "Armaggedon."
        e "There is no instructions for that spell, but there is a note."
        e "It's written poorly but I can read my father's handwriting."
        e "Cataclysm category : Wipes every living being's memory to the user's... will..."
        scene black
        scene EB7
        image EB7 = im.Scale ("EB7.png", 1920, 1080)
        with fade
        e "Wait..."
        m "So... this is what happened."
        scene black
        scene EB8
        image EB8 = im.Scale ("EB8.png", 1920, 1080)
        with fade
        e "This spell was used in the past 20 years ago to create a fake war, and a hatred towards your kind."
        e "I do remember the humans I met being kind and really well behaved."
        e "That would make sense! But this spell needs an Atrocious amount of mana!"
        scene black
        scene EB6
        image EB6 = im.Scale ("EB6.png", 1920, 1080)
        with fade
        e "No simple mage could've used it, and most importantly..."
        e "Who could have used it..."
        e "I feel like this book gets new pages each time depending on what the owners of the book know about the past."
        scene black
        scene EB4
        image EB4 = im.Scale ("EB4.png", 1920, 1080)
        with fade
        e "[name], we need to sort this clear, we'll tell Lou tomorrow, and we'll be able to begin looking for clues!"
        m "You're damn right!"
        m "...Damn, I feel totally worn out..."

        if ELove >= 10:
            e "Well... m-maybe you can... you know..."
            e "Spend the night here... with me...?"
            menu :

                "I'd love to":
                    $ELove += 2
                    scene black
                    scene EB16
                    image EB16 = im.Scale ("EB16.png", 1920, 1080)
                    with fade
                    e "GREAT!"
                    with vpunch
                    scene black
                    scene EB15
                    image EB15 = im.Scale ("EB4.png", 1920, 1080)
                    with fade
                    e "S-Sorry, I mean nice... I don't want you to pass out outside..."
                    e "Even though you live at ... 2 minutes from here."
                    e "Let me just... change quickly and I'll join you in the bed."
                    m "So I won't get the Sofa tonight?"
                    scene black
                    scene EB17
                    image EB17 = im.Scale ("EB16.png", 1920, 1080)
                    with fade
                    e "Apparently."
                    jump ESleepD3

                "Refuse":
                    scene black
                    scene EB15
                    image EB15 = im.Scale ("EB15.png", 1920, 1080)
                    with fade
                    e "O-Oh..."
                    e "I-I see..."
                    e "Either way... Thanks for being here [name]."
                    e "Having you with me is truly reassuring."
                    m "I am glad you feel that way..."
                    e "See you [name]."
                    scene black
                    "You wave back at the elf and get home."
                    "You get into your room, without even checking on Vanessa and Lou."
                    "You feel too weak anyway."
                    "You just lay on your bed and instantly fall asleep..."
                    jump DreamD3

        else:
            scene black
            scene EB14
            image EB14 = im.Scale ("EB14.png", 1920, 1080)
            with fade
            e "You should get home [name], we'll continue tomorrow."
            e "See you [name]."
            scene black
            "You wave back at the elf and get home."
            "You get into your room, without even checking on Vanessa and Lou."
            "You feel too weak anyway."
            "You just lay on your bed and instantly fall asleep..."
            jump DreamD3


    label ESleepD3:
        scene black
        scene EB18
        image EB18 = im.Scale ("EB18.png", 1920, 1080)
        with fade
        e "You look absolutely exhausted..."
        e "I'm sorry, I shouldn't have put you through a spell that powerful."
        e "You're still not used to feel mana."
        m "It's fine, nothing a good night can't fix."
        m "Especially when it's next to you..."
        e "..."
        e "No... I need to take care of you."
        m "Hm ?"
        e "C-can you close your eyes for a sec, trust me."
        scene black
        "You follow her lead and close your eyes."
        "While you slowly feel yourself slipping away, you also feel something soft."
        "Hot on your crotch, slowly moving."
        e "Y-you can open your eyes."
        scene vid C
        "The moon shines unusualy bright on Elise's face, it's appeasing to see."
        e "I-I'm not used to do this, I don't know much about that kind of stuff... you know."
        e "But Apparently guys like it."
        m "I do like it."
        e "O-Oh great, I'll keep going then."
        e "..."
        e "I-I think I'm getting used to it, it sort of feels good!"
        scene vid D
        "You slowly feel the atmosphere une the room changing."
        e "F-Fuck! Why do I feel so good?!"
        e "What are you doing to me? [name]"
        e "Please Finish whenever you want, I want you to feel good."
        e "I want you to feel good with me as much as I feel good with you!"
        "..."
        scene black
        scene EB9
        image EB9 = im.Scale ("EB9.png", 1920, 1080)
        with fade
        e "...!"
        "You can still feel Elise's soft and warm breath on your shaft."
        scene black
        scene EB10
        image EB10 = im.Scale ("EB10.png", 1920, 1080)
        with fade
        e "T-That was amazing!"
        e "I don't know If that helped you but I too feel exhausted now!"
        m "It did, I'm just glad to be with you right now."
        scene black
        scene EB11
        image EB11 = im.Scale ("EB11.png", 1920, 1080)
        with fade
        e "... I'm sorry I doubted my feelings this morning, I care about you and the rest don't matter."
        m "It's fine, I understand, what matters know is the task ahead."
        e "You're right, but one thing at a time."
        scene black
        scene EB12
        image EB12 = im.Scale ("EB12.png", 1920, 1080)
        with fade
        e "For now I just want to sleep in my Lover's arms, and we'll take care of that book Tomorrow."
        m "Lovers uh, we still haven't kissed though."
        e "I can change that."
        scene black
        scene EB13
        image EB13 = im.Scale ("EB13.png", 1920, 1080)
        with fade
        m "...!"
        "Elise's lips are, incredibly soft, warm and sweet..."
        scene black
        scene EB10
        image EB10 = im.Scale ("EB10.png", 1920, 1080)
        with fade
        e "That's that out of the way."
        m "I might want it back in my way at some point."
        e "Don't worry, I'd love to be in your way..."
        e "Anyway, Sweet dreams [name]..."
        scene black
        m "You too Elise."
        $NightEliseD3 = True

        "You both finally fall asleep..."
        jump DreamD3


    label DreamD3:
        stop music fadeout 1.0
        scene black
        ef "Elise!"
        ef "Come on! Lilian is waiting for us!"
        e "I'm coming, I'm coming..."
        play music "Ambition.mp3"
        scene black
        scene DD1
        image DD1 = im.Scale ("DD1.png", 1920, 1080)
        with fade
        ef "Still wearing your mother's robe uh?"
        e "Yeah..."
        ef "You remind me of your mother you know."
        e "I'm really curious, on how both of you met."
        ef "Oh Little sun, this was the best day of my life let me tell you."
        ef "Although, that is a story for another day!"
        ef "Come on Lilian is waiting for u-."
        scene black
        scene DD2
        image DD2 = im.Scale ("DD2.png", 1920, 1080)
        with fade
        lm "Heya nerd, oh and Elise!"
        scene black
        scene DD3
        image DD3 = im.Scale ("DD3.png", 1920, 1080)
        with fade
        lm "You look absolutely beautiful little one."
        e "T-thanks..."
        ef "I already told you!"
        scene black
        scene DD2
        image DD2 = im.Scale ("DD2.png", 1920, 1080)
        with fade
        ef "Don't call me like that."
        lm "But it suits you Heli, always with your nose your boring books~!"
        ef "Ugh, anyway, how is Marcus?"
        scene black
        scene DD4
        image DD4 = im.Scale ("DD4.png", 1920, 1080)
        with fade
        lm "Well you know him, always out to explore the world, since the day I got pregnant..."
        lm "He's so excited about life, I'm impressed by how his view of the world changed."
        lm "Although I didn't recieve anything from him in weeks... It worries me."
        ef "I'm sure he's fine."
        lm "Anyway, what's your plan for today?"
        ef "Hmm, I thought about going to the lake with Elise... apparently shady business happened there."
        scene black
        scene DD5
        image DD5 = im.Scale ("DD5.png", 1920, 1080)
        with fade
        e "You promised to teach me that Northern tribe spell!"
        ef "Of course little sun... don't worry I'll teach you that spell there!"
        scene black
        scene DD4
        image DD4 = im.Scale ("DD4.png", 1920, 1080)
        with fade
        lm "By the way Heli' I haven't heard much of Athael lately, what happened?"
        ef "Well you know him, since we opened up to mankind..."
        ef "Let's just say he's not really into 'Humans'."
        lm "A Shame, a mage of his capacity could be useful to everyone."
        scene black
        scene DD6
        image DD6 = im.Scale ("DD6.png", 1920, 1080)
        with fade
        lm "Anyway, let's go, I can't wait to hear the water flow."
        scene black
        ef "You're right, let's go."
        "..."
        stop music fadeout 1.0
        "BLINDED"
        "BY"
        "THE"
        "SUN"
        "THEY"
        "CANNOT"
        "SEE"
        "THE"
        "LIE."

        if NightEliseD3 == True:
            e "Wake up, Sleepy head!"
            play music "blackbird.mp3"
            m "Hmm..."
            scene black
            scene EM2
            image EM2 = im.Scale ("EM2.png", 1920, 1080)
            with fade
            m "Hey, little sun."
            m "How was the night?"
            scene black
            scene EM1
            image EM1 = im.Scale ("EM1.png", 1920, 1080)
            with fade
            e "Warm, sweet, I haven't slept that well in years! How was yours?"
            m "I would call being awake by the girl you love, a perfect way to end that night."
            e "I'm glad, come on let's dress up, or we'll be late."
            m "A shame I could be used to see you naked."
            e "And I could be used to please you the same way as yesterday..."
            e "But not now!"
            e "Come on [name]!"
            scene black
            "You get on your two feet, sat on the edge of the bed."
            "You stretch for a bit, and you finally decide to dress up."
            scene black
            scene EM3
            image EM3 = im.Scale ("EM3.png", 1920, 1080)
            with fade
            "You glance quickly at Elise, you notice her generous and cute curves."
            e "... Hm?"
            scene black
            scene EM4
            image EM4 = im.Scale ("EM4.png", 1920, 1080)
            with fade
            e "You can't keep your eyes out of me for a few minutes, can you?"
            m "Seems like I can't."
            e "Well dear, you will have to because we gotta spend that morning in class!"
            e "Beside you still owe me a date!"
            m "(Shit I totally forgot about it!)"
            scene black
            "You both dress up and take the road, it's a bit cold, a natural autumn morning!"
            scene black
            scene EM5
            image EM5 = im.Scale ("EM5.png", 1920, 1080)
            with fade
            e "I had a nice dream..."
            "Elise stops walking, and seems to look at you, you notice a spark of joy and nostalgia in her eyes."
            m "What was it about?"
            scene black
            scene EM6
            image EM6 = im.Scale ("EM6.png", 1920, 1080)
            with fade
            e "I was back at the lake near my place with my father, and Lilian, it felt like a flashback."
            e "My father and Lilian were studying the place, while my father teached me a spell, I still have some trouble remembering the name of it though."
            e "But I mean, it's just a dream!"
            m "(Hm, I remember this dream too... Although that lake was barely mentioned...)"
            "You both walk once again, your steps seems a bit heavier..."
            menu :

                "Tell her about your dream":
                    $ELove += 1
                    m "That's quite funny, because I had weird dream."
                    scene black
                    scene EM7
                    image EM7 = im.Scale ("EM7.png", 1920, 1080)
                    with fade
                    e "Oh, what was it about."
                    m "I was... your father, and you were standing by my side, I also recognized Lilian, with her redhair."
                    m "Your father talked about shady stuff happening at a lake."
                    m "I wonder, if it is truly a coincidence..."
                    scene black
                    scene EM8
                    image EM8 = im.Scale ("EM8.png", 1920, 1080)
                    with fade
                    e "Hm..."
                    e "I doubt it."
                    e "That grimoire may have altered our mana more than I thought."
                    m "By the way, where is the grimoire?"
                    scene black
                    scene EM9
                    image EM9 = im.Scale ("EM9.png", 1920, 1080)
                    with fade
                    e "I hid it under a mana veil, on my table, but don't worry I can summon it at any time, I don't want anyone to find out about it."
                    m "What about our friends?"
                    e "Hm... You're right, we'll have to talk about it to them."
                    e "But not now, for now let's just get to class, and we'll see how things go."
                    e "Lou should be the only one to be aware of our discovery for now."
                    m "I agree."
                    scene black
                    "You keep walking with Elise up to the academy's gates."
                    jump AcademyD4

                "Avoid the subject for now":
                    m "That's cute indeed."
                    m "By the way, where is the grimoire?"
                    scene black
                    scene EM9
                    image EM9 = im.Scale ("EM9.png", 1920, 1080)
                    with fade
                    e "I hid it under a mana veil, on my table, but I can summon it at any time, I don't want anyone to find out about it."
                    m "What about our friends?"
                    e "Hm... You're right, we'll have to talk about it to them."
                    e "But not now, for now let's just get to class, and we'll see how things go."
                    e "Lou should be the only one to be aware of our discovery for now."
                    m "I agree."
                    scene black
                    "You keep walking with Elise up to the academy's gates."
                    jump AcademyD4

        play music "blackbird.mp3"


        "You slowly wake up..."
        "Lou and Vanessa don't seem to be here, looks like you're late."
        "You grab your stuff, dress up and head to class."
        "The wind is cold, but in a nice way."
        "You finally reach the gates alongside Elise."
        jump AcademyD4

    label AcademyD4:
        "A small white fog seem to surround the establishment."
        scene black
        scene D4M
        image D4M = im.Scale ("D4M.png", 1920, 1080)
        with fade
        l "Finally here you are!"
        l "So... What were you two doing last night?"
        v "Is it really our business Lou?"
        l "No, but I am quite curious!"
        scene black
        scene D4M2
        image D4M2 = im.Scale ("D4M2.png", 1920, 1080)
        with fade
        e "Nothing special, you know, work and stuff."
        m "Yeeeeah... right."
        l "Doesn't sound too convincing, don't worry I was just messing around with you."
        "Lou seems to hide a bit of excitment as well, after all she's the one who sent you both in that library yesterday..."
        v "I was worried [name]... You could've called atleast."
        m "Sorry..."
        v "Hm... It's fine but think about me next time."
        m "(That sounded weird.)"
        menu :
            "Be kind":
                $VLove += 1
                m "I'm sorry Vanessa."
                m "I don't know what I could do without you too so you know."
                m "I understand."
                scene black
                scene D4M3
                image D4M3 = im.Scale ("D4M3.png", 1920, 1080)
                with fade
                v "Good..."
                m "Anyway, let's get inside, it's quite cold here."
                l "I wouldn't have imagined a bit of wind could vainquish you [name]."
                m "Well, it can't, but if you keep that arrogant tone you just might."
                l "I'll keep that in mind."
                "(Lou seem quite relaxed, always having her smug grin when she's mocking me)"
                "(It's weird, it feels like she has always been a part of our small family with Vanessa.)"
            "Change the subject":
                scene black
                scene D4M3
                image D4M3 = im.Scale ("D4M3.png", 1920, 1080)
                with fade
                m "Anyway, let's get inside, it's quite cold here."
                l "I wouldn't have imagined a bit of wind could vainquish you [name]."
                m "Well, it can't, but if you keep that arrogant tone you just might."
                l "I'll keep that in mind."
                "(Lou seem quite relaxed, always having her smug grin when she's mocking me)"
                "(It's weird, it feels like she has always been a part of our small family with Vanessa.)"
        scene black
        scene D4M4
        image D4M4 = im.Scale ("D4M4.png", 1920, 1080)
        with fade
        "You recognize Himia on your right, waving happily at you."
        "You also see her brother, although, something seems odd about him."
        "You also notice Chumee and another goblin with her probably one of her sisters."
        scene black
        scene D4M5
        image D4M5 = im.Scale ("D4M5.png", 1920, 1080)
        with fade
        c "Hey guys!"
        c "I'll talk to you later Dai."
        scene black
        scene D4M6
        image D4M6 = im.Scale ("D4M6.png", 1920, 1080)
        with fade
        c "How are y'all doing?"
        l "Oh we are all doing great!"
        l "Except [name], the poor thing is cold."
        if ELove >= 14 and NightEliseD3 == True:
            scene black
            scene D4M6
            image D4M6 = im.Scale ("D4M6.png", 1920, 1080)
            with fade
            e "Well I can warm him up."
            c "Oh you're quite lucky [name] it seems like the noble Wood elf got something for you."

        elif CLove >= 8:
            scene black
            scene D4M7
            image D4M7 = im.Scale ("D4M7.png", 1920, 1080)
            with fade
            c "Well, maybe I can warm him up."
            e "I doubt such a small body can warm much."
            scene black
            scene D4M8
            image D4M8 = im.Scale ("D4M8.png", 1920, 1080)
            with fade
            c "That's knowing me poorly Elise, you know how hot I am!"

        elif VLove >= 12:
            scene black
            scene D4M9
            image D4M9 = im.Scale ("D4M9.png", 1920, 1080)
            with fade
            "(Lou seems to look at Vanessa, their gaze crosses)"
            scene black
            scene D4M10
            image D4M10 = im.Scale ("D4M10.png", 1920, 1080)
            with fade
            v "I guess... I can warm him up."
            c "Oh you're so shy, that's adorable!"
        scene black
        "It just feels so nice."
        "Being surrounded by people you care, maybe some of them you love."
        scene black
        scene D4M11
        image D4M11 = im.Scale ("D4M11.png", 1920, 1080)
        with fade
        l "Do you guys know that, Vanessa was able to cast the same spell as [name]?"
        if VLove <=10:
            v "I did failed at first, but I kept working on it and I managed to lit it for a second!"

        scene black
        "This world is beautiful."
        "Isn't it [name]?"
        scene black
        scene D4M10
        image D4M10 = im.Scale ("D4M10.png", 1920, 1080)
        with fade

        e "Wow, Really ?!"
        e "I'm so proud of you!"
        e "How was the flame?"
        stop music fadeout 1.0

        scene black
        "But..."
        "Sometimes."
        scene black
        scene D4M13
        image D4M13 = im.Scale ("D4M13.png", 1920, 1080)
        with fade

        v "Well it had a really nice color."
        scene black
        scene D4M14
        image D4M14 = im.Scale ("D4M14.png", 1920, 1080)
        with fade
        v "It was purp-"
        scene black
        scene D4M15
        image D4M15 = im.Scale ("D4M15.png", 1920, 1080)
        with fade

        "The world and it's inhabitants."
        "Might prefer chaos over peace."

        m "..."
        m "What..?"
        m "There is no sound... what happened?"
        e "VANESSA?!"
        with vpunch

        l "SHIT!"
        m "..."
        scene black
        scene D4M16
        image D4M16 = im.Scale ("D4M16.png", 1920, 1080)
        with fade

        h "WHAT ARE YOU DOING?!"
        Ele "The right thing."
        Ele "These primates are all the same."
        Ele "They attacked us, tried to rape our mother."
        Ele "They killed our father."
        Ele "I am correcting the mistake we made a few weeks ago."

        m "Vanessa?"
        m "(It's so blurry, what is happening?)"
        "Your vision finally clears up, and the fog slowly fade out."
        scene black
        scene D4M17
        image D4M17 = im.Scale ("D4M17.png", 1920, 1080)
        with fade
        "The warm, colors of the sunrise are back on the courtyard."
        menu :
            "(This choice will have major consequences) "
            "They all hate us anyway.":
                $AngerD4 = True
                scene black
                "As if it was a reflex."
                "You point your arm at the agressor."
                scene black
                scene D4M18
                image D4M18 = im.Scale ("D4M18.png", 1920, 1080)
                with fade
                "The sky seem like an illusion, no one else seem to notice it."
                ef "(YOU WILL PAY, FOR WHAT YOU DID!)"
                "The voice resonate inside your mind."
                m "YOU WILL PAY, FOR WHAT YOU DID!!"
                with vpunch
                h "Wait!-"
                scene black
                scene D4M19
                image D4M19 = im.Scale ("D4M19.png", 1920, 1080)
                with fade
                e "Don't."
                e "I'll handle it, elf, against elf."
                scene black
                scene D4M20
                image D4M20 = im.Scale ("D4M20.png", 1920, 1080)
                with fade
                m "He attacked her, I have to do something."
                with vpunch
                m "HE HAS TO PAY!"
                "Your cold tone seem to worry Elise."
                scene black
                scene D4M21
                image D4M21 = im.Scale ("D4M21.png", 1920, 1080)
                with fade
                e "Believe me... He will."
                scene black
                "Himia runs at your side..."
                h "I'll take her to the infirmary."
                h "... I'm sorry."
            "I must protect Vanessa.":
                m "V...Vanessa."
                scene black
                "You feel Vanessa's skin with the back of your hand."
                "It's... cold, but you can still feel her heart beat."
                scene black
                scene D4M22
                image D4M22 = im.Scale ("D4M22.png", 1920, 1080)
                with fade
                "A blue circle seem to have appeared above Vanessa's chest."
                "You notice a warming smile as the circle appears."
                ef "Stay with me... Elena..."
                scene black
                scene D4M23
                image D4M23 = im.Scale ("D4M23.png", 1920, 1080)
                with fade
                m "Stay with me..."
                e "... I'll handle it."
                scene black
                "Himia runs at your side..."
                h "I'll take her to the infirmary."
                h "... I'm sorry."
    "You join Himia to the infirmary with Chumee and Lou."
    "Elise remains."
    "Alone."
    scene black
    scene D4M24
    image D4M24 = im.Scale ("D4M24.png", 1920, 1080)
    with fade
    ukn "What's going on Ophe~?"
    ukn "Seems like two pointy ears got in a fight."
    ukn "But you usually don't care about elves."
    ukn "this academy is the only one in the coutnry accepting humans."
    ukn "A human might've done something they qualified as 'Worthy to fight' over."
    ukn "Hm... Bor-"
    ukn "shh."
    scene black
    scene D4M25
    image D4M25 = im.Scale ("D4M25.png", 1920, 1080)
    with fade
    "The courtyard is absolutly calm."
    "No noises."
    "Not a single sound..."
    "Elise face's the agressor."
    "Her look wipes the courtyard."
    scene black
    scene D4M26
    image D4M26 = im.Scale ("D4M26.png", 1920, 1080)
    with fade
    Ele "Move, let me finish the job."
    play music "Ambition.mp3"
    scene black
    scene D4M27
    image D4M27 = im.Scale ("D4M27.png", 1920, 1080)
    with fade
    e "You're bold to talk about finishing a murder in a public place."
    scene black
    scene D4M26
    image D4M26 = im.Scale ("D4M26.png", 1920, 1080)
    with fade
    Ele "And you're dumb for not siding with your kind, she's but an ant."
    Ele "Now move."
    scene black
    scene D4M28
    image D4M28 = im.Scale ("D4M28.png", 1920, 1080)
    with fade
    e "I won't."
    e "Fight me if you want to get her."
    Ele "Nonsense, I was born in the highest Northern family."
    e "Then, go ahead, fight me."
    e "We are noble, the elves."
    e "Oh yes... we did so many things."
    e "And yet after all these years."
    e "We are still heading down."
    scene black
    scene D4M26
    image D4M26 = im.Scale ("D4M26.png", 1920, 1080)
    with fade
    Ele "You sound like the Traitor."
    Ele "Maybe you're his famous daughter."
    e "..."
    scene black
    scene D4M28
    image D4M28 = im.Scale ("D4M28.png", 1920, 1080)
    with fade
    e "It doesn't matter who I am."
    e "Look at yourselves..."
    e "ALL OF YOU."
    scene black
    scene D4M29
    image D4M29 = im.Scale ("D4M29.png", 1920, 1080)
    with fade
    e "You think you act for the greater good."
    e "That Humans are scum and so their life is but the same as an ant."
    scene D4M30
    image D4M30 = im.Scale ("D4M30.png", 1920, 1080)
    with fade
    e "That war turned you all into animals, monsters."
    scene black
    scene D4M31
    image D4M31 = im.Scale ("D4M31.png", 1920, 1080)
    with fade
    Ele "You fucking bitch how dare you insult us?!"
    scene black
    scene D4M32
    image D4M32 = im.Scale ("D4M32.png", 1920, 1080)
    with fade
    e "Mind your tongue, you're no one, you're but a small ball of hatred in a great world of love."
    e "If you can't accept humans, you can't accept peace, if you can't accept peace."
    e "You can't be accepted yourself."
    e "You said humans attacked you."
    e "So you decided to attack an innocent girl, that never even heard of them."
    e "That probably was merely a child when it happened."
    e "And yet you manage to find pride out of it."
    scene black
    e "Interesting."
    Ele "..."
    scene black
    scene D4M29
    image D4M29 = im.Scale ("D4M29.png", 1920, 1080)
    with fade
    e "You all feed a cycle of vengeance, of hatred."
    e "You are not different from the monsters we used to fight."
    e "But I know one thing, I know that someone attacking a young innocent girl in the back is nothing but a coward."
    scene black
    scene D4M30
    image D4M30 = im.Scale ("D4M30.png", 1920, 1080)
    with fade
    e "Your titles means nothing to me, if you attack anyone else innocent here, elf, human, goblin, dwarf, I don't care."
    scene black
    ef "You've grown."
    ef "Little sun."
    scene D4M33
    image D4M33 = im.Scale ("D4M33.png", 1920, 1080)
    with fade
    e "You'll have to fight me."
    "..."
    scene D4M34
    image D4M34 = im.Scale ("D4M34.png", 1920, 1080)
    with fade
    "No sound..."
    "The crowd will remember that speech and your actions."
    stop music fadeout 1.0
    scene black

    "The infirmary is the same as the rest of the academy; very traditional."
    "You couldn't tell the difference between this infirmary and any other."
    "Himia carries Vanessa gently in from outside, and slowly lays her down on one of the beds."
    l "... I'll look for Elise, we left her alone."
    c "I'll come with you."
    scene black
    scene D4I
    image D4I = im.Scale ("D4I.png", 1920, 1080)
    with fade
    h "..."
    h "I'm sorry [name]."
    scene black
    scene D4I2
    image D4I2 = im.Scale ("D4I2.png", 1920, 1080)
    with fade
    h "I-I don't know why he did that."
    menu :
        "Himia helped me until now, I don't really know how I feel toward her yet though."
        "Accept her apologies":
            $HLove += 2
            m "I...I don't know, Himia, you're kind to me."
            m "But what tells me it's not all a lie?"
            m "Your mad brother can just come back and finish the job."
            scene black
            scene D4I7
            image D4I7 = im.Scale ("D4I7.png", 1920, 1080)
            with fade
            h "..."
            h "...Eleon was... different... before."
            h "My Mother, she was everything for him."
            h "And the day the humans took her."
            h "Something changed."
            m "All of that for a lie."
            h "Hmm ?"
            m "N-Nothing."
            m "You don't need to apologize Himia, you helped, you didn't try to attack Vanessa, you helped even."
            scene black
            scene D4I3
            image D4I3 = im.Scale ("D4I3.png", 1920, 1080)
            with fade
            h "Thanks [name]..."
            h "I'll make it up to you, to both of you, I promise."
            scene black
            "Himia leaves the room, her face still torn by the remorse, but you somehow see a spark of hope in her eyes."


        "Reject her apologies":
            m "You're SORRY?!"
            scene black
            scene D4I4
            image D4I4 = im.Scale ("D4I4.png", 1920, 1080)
            with fade
            m "Vanessa is the only family I have left in my life!"
            m "The only landmark I had in this blasted world!"
            m "We're not related by blood, but I would gladly consider her my Sister."
            m "What If I killed that bastard in front of you, FOR NO REASONS."
            m "Elves also took my parents you know!"
            h "..."
            m "They came, used their twisted spells and took away everyone."
            m "Ripped their will away and made them slaves for your kind."
            scene black
            scene D4I5
            image D4I5 = im.Scale ("D4I5.png", 1920, 1080)
            with fade
            "Is that a Lie?"
            "You know that it is, so why are you saying it?"
            "Does the fact that it's a lie still make it a valid excuse?"
            "The lie you tell yourself, to make that innocent girl suffer?"
            m "They probably died like dogs, same as every other humans that were captured at the time."
            m "Some died... tortured physically."
            m "Some died after being tortured mentally."
            m "Forced to see their loved one slaughtered, again, and again, and again, until in the depth of their despair the victim prefered to slice their chest open."
            m "They'd rather die than see anyone else murdered."
            scene black
            scene D4I6
            image D4I6 = im.Scale ("D4I6.png", 1920, 1080)
            with fade
            h "I...I'll..."
            "Your 'speech' seem to have shook Himia."
            m "No, you both did enough."
            h "...I'll leave you two alone, I hope you'll find a way to forgive us."
            m "I hope I'll find a way to forgive YOU."
            m "I hope, that I'm saying all of that out of anger for the situation."
            m "And not because I hate you."
            h "..."
            scene black
            "Himia leaves the room, you somehow feel bad, perhaps it was too harsh... or was it just enough..."
    ukn "Oh... Poor Himia she seems devastated."
    m "Hm ?"
    scene black
    scene D4I8
    image D4I8 = im.Scale ("D4I8.png", 1920, 1080)
    with fade
    ukn "Oh I'm sorry! You probably don't know me."
    ukn "I'm Delphine, the Academy's nurse."
    play music "born.mp3"
    scene black
    scene D4I9
    image D4I9 = im.Scale ("D4I9.png", 1920, 1080)
    with fade
    doc "I heard what happened in the courtyard, sometimes I wonder how can the world be so cruel."
    scene black
    scene D4I10
    image D4I10 = im.Scale ("D4I10.png", 1920, 1080)
    with fade
    doc "I'll do my best to get your friend up on her feet!"
    doc "It would be a shame to see future great human mages die that young!"
    scene black
    scene D4I11
    image D4I11 = im.Scale ("D4I11.png", 1920, 1080)
    with fade
    "The doctor glitters with hope and good feelings."
    "She somehow feels really naïve and yet, has enough charisma to make you smile."
    "As Cold as the last sentence was, you can only hope for the best."
    doc "For now, I will just use a small spell to locate the issue!"

    if AngerD4 == True:
        scene black
        scene D4I12
        image D4I12 = im.Scale ("D4I12.png", 1920, 1080)
        with fade
        doc "Hmm, her back is in a bad shape, but I can heal her."
        m "You can?"
        scene black
        scene D4I13
        image D4I13 = im.Scale ("D4I11.png", 1920, 1080)
        with fade
        doc "Oh of course little one, I've studied the human body for a few years now."
        doc "The human body is oddly similar to the elves, maybe tougher bones and muscle mass though."
        doc "Anyway, just take a sit on the other side, your friend is between good hands, I promise."
        scene black
        "You can but obey her demand and wait for her to do her job."

    else:
        scene black
        scene D4I12
        image D4I12 = im.Scale ("D4I12.png", 1920, 1080)
        with fade
        doc "Oh!"
        m "What?"
        scene black
        scene D4I13
        image D4I13 = im.Scale ("D4I13.png", 1920, 1080)
        with fade
        doc "She already seems quite advanced in her regeneration!"
        doc "Say, has one of your friend applied a spell on her?"
        scene black
        scene D4I14
        image D4I14 = im.Scale ("D4I14.png", 1920, 1080)
        with fade
        m "I do remember a magic circle above her chest."
        doc "Well it's impressive, it seems like it almost cured her instantly, I don't even have to do anything."
        doc "Who did it?"
        m "I think I did."
        scene black
        scene D4I15
        image D4I15 = im.Scale ("D4I15.png", 1920, 1080)
        with fade
        doc "You?"
        m "Yeah."
        doc "I wouldn't dare mock you, but you're an amateur, how can a human draw a circle that complex and that perfectly?"
        m "I don't know, I just 'Did'."
        scene black
        scene D4I16
        image D4I16 = im.Scale ("D4I16.png", 1920, 1080)
        with fade
        doc "Weird, but impressive! Your specie is full of surprises!"
        doc "I wish I could get some sample from your body."
        m "Uh..."
        scene black
        scene D4I17
        image D4I17 = im.Scale ("D4I17.png", 1920, 1080)
        with fade
        doc "I'm sorry sometimes my thirst for science makes everything quite... awkward."

    scene black
    scene D4I16
    image D4I16 = im.Scale ("D4I16.png", 1920, 1080)
    with fade
    doc "By the way! The principal told me that she wanted to see you and Eleon in her office once you're done here."
    doc "Your friend should wake up soon, so please do stay a bit, I'm sure she would love to see you first!"
    m "Sure!"
    scene black
    scene D4I18
    image D4I18 = im.Scale ("D4I18.png", 1920, 1080)
    with fade
    doc "I'll leave you two alone, oh by the way, what's your name?"
    m "[name]"
    doc "[name]!"
    stop music fadeout 1.0
    doc "Bye!"
    scene black
    "You wave back at the doc, and stare at Vanessa."
    scene black
    scene D4I
    image D4I = im.Scale ("D4I.png", 1920, 1080)
    with fade
    "She seem so peaceful, as if nothing happened."
    "As if she just fell asleep."

    v "Hm..."
    scene black
    scene D4I19
    image D4I19 = im.Scale ("D4I19.png", 1920, 1080)
    with fade
    v "...[name]?"
    m "Vanessa?"
    scene black
    scene D4I20
    image D4I20 = im.Scale ("D4I20.png", 1920, 1080)
    with fade
    v "...W-What happened?"
    menu :

        "Avoid the question":
            m "It's not important, God, Vanessa I was so worried!"
            scene black
            scene D4I21
            image D4I21 = im.Scale ("D4I21.png", 1920, 1080)
            with fade
            v "Hey don't worry, I'm here."
            v "I'll never leave you."
            m "I'm just glad you're ok."

        "Tell her bluntly":
            stop music fadeout 1.0
            $VLove += 1
            m "Himia's brother tried to... kill you."
            scene black
            scene D4I22
            image D4I22 = im.Scale ("D4I22.png", 1920, 1080)
            with fade
            v "What? Why? How?"
            m "I don't know he used a spell behind your back."
            scene black
            scene D4I23
            image D4I23 = im.Scale ("D4I23.png", 1920, 1080)
            with fade
            v "..."
            v "Really?"
            m "Yeah..."
            scene black
            scene D4I24
            image D4I24 = im.Scale ("D4I24.png", 1920, 1080)
            with fade
            v "We're not safe anymore, even here?"
            m "... You're safe with Elise."
            m "I trust her."
            v "... Me too."
            v "Thanks for your... honesty."


    m "The principal needs me in her office, maybe I should go."
    v "Well... maybe you can just... stay a bit more, I just woke up..."
    menu :

        "Sure.":
            $VLove += 1
            m "Sure, you're more important."
            play music "born.mp3"
            jump InfirmaryD4
        "I really have to go.":
            m "It is really important Vanessa, I should really go."
            scene black
            scene D4I26
            image D4I26 = im.Scale ("D4I26.png", 1920, 1080)
            with fade
            v "Oh... okay."
            scene black
            scene D4I27
            image D4I27 = im.Scale ("D4I27.png", 1920, 1080)
            with fade
            v "But come back one you're done alright?"
            m "I promise."
            scene black
            "You leave the infirmary, and head to the principal's office."
            jump OfficeD4

    label InfirmaryD4:
        scene black
        scene D4I25
        image D4I25 = im.Scale ("D4I25.png", 1920, 1080)
        with fade
        v "Thanks..."
        "Vanessa slowly gets on her feets, and walks slowly to a window."
        scene black
        scene D4I28
        image D4I28 = im.Scale ("D4I28.png", 1920, 1080)
        with fade
        m "..."
        v "You know [name]..."
        v "Sometime I wonder what would my mother think of my choices."
        m "Really? I remember your mother being quite kind."
        scene black
        scene D4I29
        image D4I29 = im.Scale ("D4I29.png", 1920, 1080)
        with fade
        v "Well I remember her being against joining you here!"
        m "Well... That's true."
        v "She would probably say something like:"
        scene black
        scene D4I30
        image D4I30 = im.Scale ("D4I30.png", 1920, 1080)
        with fade
        v "'That's what ye get for not' listenin' tae me Vanessa, yer far from me for a month and here ye are on an hospital's bed!'"
        scene black
        scene D4I31
        image D4I31 = im.Scale ("D4I31.png", 1920, 1080)
        with fade
        "Her laugh sounds so cheerful, for a moment you totally forgot what happened in the morning."
        "A simple smile, and innocent giggle you can feel your own lips following hers as a smile covers your face."
        scene black
        scene D4I32
        image D4I32 = im.Scale ("D4I32.png", 1920, 1080)
        with fade
        v "I miss her."
        m "As you should, she's your family."
        v "You're my family too, maybe not by blood, but I would still see you as part of it."
        v "And I'm glad to be a part of your life."
        m "You will always be."
        if ELove >= 14:
            scene black
            scene D4I28
            image D4I28 = im.Scale ("D4I28.png", 1920, 1080)
            with fade
            v "I know Elise already has an important place"

        elif CLove >= 8:
            scene black
            scene D4I28
            image D4I28 = im.Scale ("D4I28.png", 1920, 1080)
            with fade
            v "I know Chumee already has an important place."

        else:
            scene black
            scene D4I28
            image D4I28 = im.Scale ("D4I28.png", 1920, 1080)
            with fade
            v "And you too will always be for me."

        v "...But I sometime wonder how you see me."

        menu :

            "A friend.":
                scene black
                scene D4I33
                image D4I33 = im.Scale ("D4I33.png", 1920, 1080)
                with fade
                v "Well as long as you're happy I am, no matter who I am!"
            "My Sister":
                $VLove += 1
                scene black
                scene D4I34
                image D4I34 = im.Scale ("D4I34.png", 1920, 1080)
                with fade
                v "Awh..."
                v "That's adorable."

            "My girlfriend":
                $VLove += 2
                $GFVD4 = True
                scene black
                scene D4I35
                image D4I35 = im.Scale ("D4I35.png", 1920, 1080)
                with fade
                v "W-Wait really?"
                m "I'm messing with you!"
                scene black
                scene D4I36
                image D4I36 = im.Scale ("D4I36.png", 1920, 1080)
                with fade
                v "O-Oh... W-Well, I wouldn't mind being your girlfriend..."
                m "Really?"
                v "Yeah, We both know each other."
                v "And... I-I do like you."
                m "Me too."
                scene black
                scene D4I37
                image D4I37 = im.Scale ("D4I37.png", 1920, 1080)
                with fade
                v "I don't know what the others would think, but maybe we should try something?"
                m "Yeah, I agree."
                v "..."
                scene black
                scene D4I35
                image D4I35 = im.Scale ("D4I35.png", 1920, 1080)
                with fade
                v "Let's have a small date, just the two of us!"
                m "Oh that's sudden, I didn't know you were that direct with your feelings, that's new!"
                scene black
                scene D4I36
                image D4I36 = im.Scale ("D4I36.png", 1920, 1080)
                with fade
                v "Well maybe I recieved a little push by fate!"
                m "Sure, I'd love to spend an evening with you!"
                scene black
                scene D4I37
                image D4I37 = im.Scale ("D4I37.png", 1920, 1080)
                with fade
                v "... Thanks..."
                "Vanessa seem to smile up to her ears, seeing her that happy feels... heartwarming."
        scene black
        "You both sit on a small bench in the middle of the room."
        scene black
        scene D4I38
        image D4I38 = im.Scale ("D4I38.png", 1920, 1080)
        with fade
        v "I always wanted to be an Archmage."
        m "Always?"
        m "Quite the uncommon dream, atleast for humans."
        v "Well yeah..."
        scene black
        scene D4I39
        image D4I39 = im.Scale ("D4I39.png", 1920, 1080)
        with fade
        v "Those stories about magic wands."
        v "Fireballs, pointy hats."
        v "Water Elementals."
        v "Dadghar."
        m "(What was that last one?)"
        scene black
        scene D4I38
        image D4I38 = im.Scale ("D4I38.png", 1920, 1080)
        with fade
        v "That fantasy around magic, it's just wonderful..."
        v "When I managed to use that simple spell, with the flame, I felt like I could do so much."
        m "I don't doubt your capacity Vanessa, I'm sure you'll be a great mage."
        scene black
        scene D4I40
        image D4I40 = im.Scale ("D4I40.png", 1920, 1080)
        with fade
        v "And so will you!"
        m "You should ask Elise to teach you some stuff!"
        scene black
        scene D4I41
        image D4I41 = im.Scale ("D4I41.png", 1920, 1080)
        with fade
        v "You think?"
        m "Well, I'm sure she would love to help you."
        scene black
        "You spend a few minutes talking with Vanessa."
        scene black
        scene D4I42
        image D4I42 = im.Scale ("D4I42.png", 1920, 1080)
        with fade
        m "...Hmm I should go."
        v "Awh..."
        m "Don't worry, I'll come back to check on you as soon as I'm done!"
        scene black
        scene D4I43
        image D4I43 = im.Scale ("D4I43.png", 1920, 1080)
        with fade
        doc "Oh... you two are still here!"
        m "Oh I was about to leave."
        doc "Oh and your friend is already standing on her feets!"
        doc "What's your name butterfly?"
        m "(That sounds childhish... sort of?)"
        v "Vanessa!"
        v "Wow, your hair looks beautiful!"
        scene black
        scene D4I44
        image D4I44 = im.Scale ("D4I44.png", 1920, 1080)
        with fade
        v "I-I mean."
        doc "Oh you're so sweet, I like your hairstyle too, here I'll make a few tests to see how your body is holding up, alright."
        v "Sure!"
        scene black
        "You wave kindly to Vanessa, and head to your trial."

    label OfficeD4:
        stop music fadeout 1.0
        "You step inside Headmistress's office."
        "Nothing out of the ordinary."
        "Although you do notice a window where a wall should be."
        "Strange."
        "You notice Eleon sat on a chair."
        play music "Nobility.mp3"
        scene black
        scene D4O
        image D4O = im.Scale ("D4O.png", 1920, 1080)
        with fade
        P "Ah! [name], we've been waiting for you."
        m "I apologize, I wanted to make sure my... friend was alright."
        P "You do not have to worry about it."
        scene black
        "You can feel shivers down your spine, as you clunch your fist and sit next to him."
        scene black
        scene D4O2
        image D4O2 = im.Scale ("D4O2.png", 1920, 1080)
        with fade
        P "So, I didn't call you here to chat."
        m "I guessed so."
        P "... Indeed."
        scene black
        scene D4O3
        image D4O3 = im.Scale ("D4O3.png", 1920, 1080)
        with fade
        P "Mr.[name], I, Principal Elisandre of the Ancient tribe-"
        scene black
        scene D4O4
        image D4O4 = im.Scale ("D4O4.png", 1920, 1080)
        with fade
        Ele "Let's get this over with!"
        Ele "We don't have any time to loose with titles, we all know how great you are."
        scene black
        scene D4O5
        image D4O5 = im.Scale ("D4O5.png", 1920, 1080)
        with fade
        P "You will learn Respect Boy."
        P "As I was saying, Mr.[name]."
        scene black
        scene D4O3
        image D4O3 = im.Scale ("D4O3.png", 1920, 1080)
        with fade
        P "Due to the event that happened this morning, we cannot keep you here."
        m "What?!"
        m "It doesn't make any sense! He attacked my friend!"
        scene black
        scene D4O2
        image D4O2 = im.Scale ("D4O2.png", 1920, 1080)
        with fade
        P "Yes, yes, Eleon, you too will be expelled for today."
        Ele "WHAT?!"
        m "WHAT?! A DAY? HE ALMOST TOOK HER LIFE!"
        with vpunch
        scene black
        scene D4O3
        image D4O3 = im.Scale ("D4O3.png", 1920, 1080)
        with fade
        P "Come on don't be ridiculous [name], humans die at 90 in most of the cases."
        m "HOW DOES IT MAKE MY LIFE LESS VALUABLE THAN HIS?!"
        with vpunch
        P "We elves live for Centuries, some even Millenials."
        m "A life is a life!"
        m "I thought we were equals!"
        scene black
        scene D4O2
        image D4O2 = im.Scale ("D4O2.png", 1920, 1080)
        with fade
        P "Don't be foolish, You can't compare Goblins or us to your kind."
        P "I can barely compare myself to these green 'things'"
        P "We are sooo different."
        P "Beside..."
        if AngerD4 == True:
            scene black
            scene D4O6
            image D4O6 = im.Scale ("D4O6.png", 1920, 1080)
            with fade
            P "You used a very unstable spell to fight back Eleon."
            P "You could've killed him!"
            P "If not the entire courtyard!"
            ef "I had everything under control!"
            m "I had everything under control!"
            P "A Human? Mastering a spell like that one? Don't be ridiculous."
            P "I am kind enough to not report this to the great ministry."
        else:
            scene black
            scene D4O6
            image D4O6 = im.Scale ("D4O6.png", 1920, 1080)
            with fade
            P "You used a very unstable spell to try to heal your friend!"
            P "You couldv've killed her yourself!"
            P "If not the entire courtyard!"
            ef "I had everything under control!"
            m "I had everything under control!"
            P "A Human? Mastering a spell like that one? Don't be ridiculous."
            P "I am kind enough to not report this to the great ministry."
        scene black
        scene D4O3
        image D4O3 = im.Scale ("D4O3.png", 1920, 1080)
        with fade
        P "My mind is made up, [name] you are expelled from the Pheris Academy until further notice."
        m "If we can't master magic, why are we here."
        P "..."
        scene black
        scene D4O9
        image D4O9 = im.Scale ("D4O9.png", 1920, 1080)
        with fade
        Ele "Leave now, Monkey."
        Ele "And be happy I don't want your filthy blood on my skin!"
        menu :
            "I'm boiling."
            "Ignore him, might be better":
                scene black
                "You leave the room queietly."
            "Intimidate them":
                scene black
                scene D4O7
                image D4O7 = im.Scale ("D4O7.png", 1920, 1080)
                with fade
                m "You should be glad Himia is with you."
                m "Or else I might've killed you in that courtyard."
                Ele "YOU LITTLE-"
                scene black
                scene D4O8
                image D4O8 = im.Scale ("D4O8.png", 1920, 1080)
                with fade
                P "Enough!"
                with vpunch
                P "Leave this room at once Human!"
                P "Eleon, you know he's powerless!"
                m "You can both tell you that to sleep at night."
                m "I know way more than you both do."
                ef "You are Blinded by the lie you tell yourself."
                m "You are Blinded by the lie you tell yourself."
                scene black
                "You leave the room queietly."
                "You also notice that Helirios's voice seem to resonate in your head."
                "It became somehow frequent today."
        stop music fadeout 1.5
        scene black
        scene D410
        image D410 = im.Scale ("D4O10.png", 1920, 1080)
        with fade
        m "...Hmm?"
        play music "FilledLove.mp3"
        m "Elise?"
        e "H-Hey..."
        m "You were eavesdropping?"
        e "Yeah... sort of."
        m "Guess you know how it is then."
        scene black
        scene D411
        image D411 = im.Scale ("D4O11.png", 1920, 1080)
        with fade
        e "It's unfair, I don't get it."
        m "Well me t-"
        scene black
        scene D417
        image D417 = im.Scale ("D4O17.png", 1920, 1080)
        with fade
        Ele "Arf, Finally done with him!"
        "You both seem to hear voices in the office."
        P "You're a damn pain."
        scene black
        scene D413
        image D413 = im.Scale ("D4O13.png", 1920, 1080)
        with fade
        Ele "It had to be done, I don't want to see humans around me."
        P "Well we don't have any choice, the ministry wants us to take care of them."
        Ele "We could just enslave them again!"
        P "It doesn't work like that."
        P "Enslave a population and they will one day rise."
        Ele "Humans? Come on don't be ridiculous."
        Ele "They can't do anything we're superior."
        scene black
        scene D414
        image D414 = im.Scale ("D4O14.png", 1920, 1080)
        with fade
        P "We are... But I heard reports from the central laboratory."
        P "Some humans apparently have the magical potential of archmages."
        Ele "Bullshit, and even if it's true a single sheep cannot reflect the entire herd."
        P "Maybe you're right."
        P "But the circle that human used."
        scene black
        scene D415
        image D415 = im.Scale ("D4O15.png", 1920, 1080)
        with fade
        P "I don't know why it reminds me of something."
        Ele "What?"
        P "I don't know, since the day I got the daughter of the traitor's robe..."
        P "I seem to have my head sort mixed."
        Ele "Mixed?"
        P "I feel like some stuff happened in the past, and yet they don't make sense."
        scene black
        scene D418
        image D418 = im.Scale ("D4O18.png", 1920, 1080)
        with fade

        e "...! My mother's Robe!"
        scene black
        scene D419
        image D419 = im.Scale ("D4O19.png", 1920, 1080)
        with fade
        e "That bitch! How did she got it?!"
        m "Shhh..."
        scene black
        scene D416
        image D416 = im.Scale ("D4O16.png", 1920, 1080)
        with fade
        P "Anyway, you should get back to class."
        Ele "Why though the class is boring."
        P "It's meant to be boring, we can't teach our secrets to humans."
        P "I'll schedule you to one of our true professors, in the meantime try to avoid causing trouble."
        scene black
        "Elise grabs you by the wrists and runs out of Eleon's vision while he leaves the room."
        scene black
        scene D420
        image D420 = im.Scale ("D4O20.png", 1920, 1080)
        with fade
        e "My robe! I-I don't get it."
        m "We'll get it back."
        scene black
        scene D421
        image D421 = im.Scale ("D4O21.png", 1920, 1080)
        with fade
        e "How?"
        m "I promise, we'll get it back."
        scene black
        scene D422
        image D422 = im.Scale ("D4O22.png", 1920, 1080)
        with fade
        e "That's a lot for a single day... What will you do while you're expelled?"
        m "..."
        m "I'll make a plan, to get your robe back, and finally find out who used the Armaggedon."
        m "Meet me at my place in the evening, come with Lou."
        e "Isn't it risky, what if Vanessa comes i-"
        scene black
        scene D423
        image D423 = im.Scale ("D4O23.png", 1920, 1080)
        with fade
        m "I plan on telling the truth to Vanessa."
        e "What?! You sure she can handle it, it's not just some small secret we're talking conspiracy!"
        m "The grimoire is our proof."
        scene black
        scene D424
        image D424 = im.Scale ("D4O24.png", 1920, 1080)
        with fade
        e "... you're right."
        if ELove >= 15:

            e "..."
            scene black
            e "Fuck..."
            "Elise takes you in her arms, you can feel her somehow tearing up."
            scene black
            scene D425
            image D425 = im.Scale ("D4O25.png", 1920, 1080)
            with fade
            e "I-I love you, you know that?"
            "Elise's warm embrace seems to burn the doubts away, you can just feel her warm hands against your neck and her reconforting breath against your shoulder."
            m "Me too."
        m "I'll see you later."
        e "Yeah..."
        stop music fadeout 0.5
        scene black
        "You head to the Infirmary before leaving the academy."
        "There Vanessa, Lou and Chumee seem to be talking."
        "The Doc is nowhere to be found."

        scene black
        scene D4
        image D4 = im.Scale ("D4.png", 1920, 1080)
        with fade
        v "Oh [name]!"
        v "You're back!"
        c "You definitely took your sweet time big guy."
        m "Well."
        l "So you got that bastard kicked out and the Academy is giving you their best girls to compensate for the loss?"
        scene black
        scene D41
        image D41 = im.Scale ("D41.png", 1920, 1080)
        with fade
        v "Lou!"
        l "Come on, you know I'm joking!"
        m "I'm expelled from the Academy."
        scene black
        scene D42
        image D42 = im.Scale ("D42.png", 1920, 1080)
        with fade
        play music "Mystery.mp3"
        v "WHAT!"
        c "You're not serious?"
        l "Good one [name], now show us the 1st girl they gave you."
        m "..."
        scene black
        scene D43
        image D43 = im.Scale ("D43.png", 1920, 1080)
        with fade
        l "O-Oh."
        c "But why would they do that?!"
        m "Apparently Goblins and Humans are below elves."
        m "The headmistress let that fucking piece of shit insult me and degrade me."
        m "He got expelled for a single day."
        m "They told me that humans were too different from the elves to recieve any kind of treatment."
        m "Same for Goblins."
        c "What the fuck?! Goblins have been in rather good terms with the elves for centuries why would we recieve that?"
        m "I have no idea."
        l "Hmm, what about Elise?"
        m "Saw her upstairs, let's all meet back at my place in the evening."
        c "Why?"
        scene black
        scene D44
        image D44 = im.Scale ("D44.png", 1920, 1080)
        with fade
        m "Because this school, and this whole society is a lie, and I intend to show the truth."
        v "I-I'll get home later."
        l "I'll stick here a bit longer, I wonder how Himia is holding up after what her brother did."
        c "Well I'll join you all in the evening with Lou then."
        m "Good, see you all later."
        scene black
        "You step out of the room and head for the main gate."
    stop music fadeout 1.0
    "Once outside, the establishement you wander in the city's streets."
    "So much happened in a few days."
    m "(Learning that the war never existed was a huge deal, I wonder how Vanessa will react.)"
    m "(I need to look for clues, who used the Armaggedon and modified everyon's memory.)"
    m "(It has been 30 years.)"
    m "(The grimoire seem to have an impact on my surroudings and my own memory.)"
    m "(I need a break.)"
    "You notice a café, near your place, you decide to enter."
    play music "holographic.mp3"
    scene black
    scene D4C1
    image D4C1 = im.Scale ("D4C1.png", 1920, 1080)
    with fade
    "The place seems absolutly empty."
    "You wipe the room as if you were looking for something."
    "Nothing, although you focus on two girls."
    scene black
    scene D4C2
    image D4C2 = im.Scale ("D4C2.png", 1920, 1080)
    with fade
    m "(Wait... are those... Cat ears?!)"
    m "(Hm, probably a headband or something.)"
    scene black
    scene D4C3
    image D4C3 = im.Scale ("D4C3.png", 1920, 1080)
    with fade
    "You finally sit on a table nearby, waiting for a waitress to ask you what you want."
    "The ambiance is cozy and nice for a cold morning."
    ukn "I'm impressed, the way that Elven girl stood up to her own kind!"
    ukn "Does it really matter?"
    ukn "It does, elves are usually arrogant."
    ukn "I wonder what was all that fuss about."
    ukn "Well I did heard that he attacked a human, almost killed her."
    ukn "Hm, damn bastards, they never learn."
    menu :
        "They're talking about what happened this morning!"
        "Join their conversation":
            $OLove += 1
            scene black
            scene D4C13
            image D4C13 = im.Scale ("D4C4.png", 1920, 1080)
            with fade
            "You finally decide to stand up and join the two girls."
            m "I heard you two talking about what happened this morning."
            ukn "Oh?"

        "Mind your business":
            scene black
            scene D4C4
            image D4C4 = im.Scale ("D4C4.png", 1920, 1080)
            with fade
            o "Hey!"
            o "You were at the academy this morning, right?"
            m "Yeah, how do you know that?"
            o "You still wear their uniform, silly."
            m "Oh."
            o "Come, sit here and tell us more about what happened!"
    scene black
    scene D4C5
    image D4C5 = im.Scale ("D4C4.png", 1920, 1080)
    with fade
    m "I'm the one that stood against the white haired elf."
    ukn "Oh now that's getting interesting."
    ukn "And who are you?"
    m "I'm [name]."
    ukn "Well, I'm Ophelia, and that girl with the cat ears is my friend-"
    scene black
    scene D4C6
    image D4C6 = im.Scale ("D4C4.png", 1920, 1080)
    with fade
    ukn "I'm Mine!"
    scene black
    scene D4C5
    image D4C5 = im.Scale ("D4C5.png", 1920, 1080)
    with fade
    o "Sooo, [name]."
    o "What happened, I don't often see two 'knify' ears fighting each others over human business."
    scene black
    "You take some time to precisly explain what happened."
    "How the coward attacked Vanessa from the back."
    if AngerD4 == True:
        "How you tried to fight back."
        "But got interrupted."
    else:
        "How you tried to save Vanessa, and succeeded."
    "And how Elise finally intervened and took the matter at hand."
    scene black
    scene D4C7
    image D4C7 = im.Scale ("D4C7.png", 1920, 1080)
    with fade
    mi "That 'Elise' sounds cool!"
    o "Wait a minute kitty, I don't trust those pointy ears."
    scene black
    scene D4C8
    image D4C8 = im.Scale ("D4C8.png", 1920, 1080)
    with fade
    o "Tell me more about that Redhead elf [name]."
    o "I'll tell you more about me after."
    m "Elise is the first elf I made when I joined the Academy."
    m "She's quite talented, and really kind, I do trust her."
    scene black
    scene D4C9
    image D4C9 = im.Scale ("D4C9.png", 1920, 1080)
    with fade
    o "Hm, you're foolish, Elves are scum arrogant bastards."
    mi "Come on Ophe that's mean."
    menu :

        "Defend Elise":
            $MLove += 1
            scene black
            scene D4C10
            image D4C10 = im.Scale ("D4C10.png", 1920, 1080)
            with fade
            m "Elise, has done nothing but helping me since the day I got here."
            m "She deserves my respect, and my friendship far more than I deserve hers."
            o "Hmm I remain unconvinced, but so be it, maybe you're right."
            o "You indeed seem attached to that girl."
        "Agree":
            $OLove += 1
            scene black
            scene D4C11
            image D4C11 = im.Scale ("D4C11.png", 1920, 1080)
            with fade
            m "You're right, elves are scum, arrogant assholes."
            m "I will never forgive what that bastard did to Vanessa."
            o "Hmm Vanessa, she's your friend right?"
            m "She is."
            o "Friendships are sometime weirds."

    o "Do you know Himia?"
    m "I do."
    o "Hm, she's the only elf I can tolerate."
    o "Mostly because she's litteraly a larva."
    m "A larva?"
    o "Yeah, she just reads, make weird jokes, she's a book worm."
    scene black
    scene D4C12
    image D4C12 = im.Scale ("D4C12.png", 1920, 1080)
    with fade
    o "She's the first elf I met... after..."
    m "After?"
    o "A-Anyway, not important, I understand how you feel towards the elves around you."
    o "But I gotta admit, I'm worried."
    m "I answered your questions, I have a few for you."
    scene black
    scene D4C13
    image D4C13 = im.Scale ("D4C13.png", 1920, 1080)
    with fade
    o "Shoot."
    jump QD4OM
label QD4OM:

    menu :

        "Why does your friend have cat ears?":
            scene black
            scene D4C12
            image D4C12 = im.Scale ("D4C12.png", 1920, 1080)
            with fade
            o "It's a long story, a painful one."
            o "I'm surprised you noticed those were true ears though."
            m "I didn't, I thought it was a headband."
            o "Oh... well that's a way to blow a secret."
            o "I'll tell you more when I'll feel ready."
            jump QD4OM
        "You're not studying magic?":
            scene black
            scene D4C10
            image D4C10 = im.Scale ("D4C10.png", 1920, 1080)
            with fade
            o "I don't need to, I study myself, Elven books are forbidden for Humans and Goblins."
            o "So I basically experiment myself."
            o "Beside those 'human magic academy' are purely manipulation by the governement to control human knowledge."
            jump QD4OM
        "Can I pet you, Mine?":
                scene black
                scene D4C6
                image D4C6 = im.Scale ("D4C6.png", 1920, 1080)
                with fade
                mi "Sure!"
                scene black
                scene D4C14
                image D4C14 = im.Scale ("D4C14.png", 1920, 1080)
                with fade
                "You slowly put your hand on Mine's head, her hair are awfully soft and warm."
                "They feel oddly similar to a cat."
                "Weird."
                o "Happy now?"
                mi "I definitely am."
                m "Yeah, your hair are really soft it's a bit weird."
                jump QD4OM
        "Do you know Helirios?":
                scene black
                scene D4C5
                image D4C5 = im.Scale ("D4C5.png", 1920, 1080)
                with fade
                o "Yeah the 'Traitor', the forsaken 'Autor'."
                o "Most of the books on the market by him are now foolish stories."
                o "But I know that most of his true work remains hidden."
                jump QD4OM

        "Continue":
                jump cafe2
    label cafe2:
        stop music fadeout 1.0
        scene black
        "You spend the entire morning and a huge chunk of the afternoon talking with Mine and Ophelia."
        "You learn that Ophelia is incredibly talented and is one of the first human to be able to channel important spells."
        "You also learn that Mine cannot channel anything, she cannot feel the mana, nor use it without any kind of assistance."
        scene black
        scene D4C15
        image D4C15 = im.Scale ("D4C15.png", 1920, 1080)
        with fade
        o "Oh! It's getting late, we should get home Mine!"
        scene black
        scene D4C13
        image D4C13 = im.Scale ("D4C13.png", 1920, 1080)
        with fade
        o "It was great meeting you [name]!"
        o "I'm sure we'll meet again soon!"
        mi "Bye [name]!"
        scene black
        "It's late indeed, you too decide to head home, you've got guests tonight afterall."
        stop music fadeout 1.0

        "You finally head home, Vanessa should soon join you."
        m "(How can I tell them the truth about what happened?)"
        m "(Hey, so you know the war? it never really existed.)"
        "If anything, things would get interesting tonight."
        play music "Blackbird.mp3"
        "You get home, you can see the reassuring light of the sunset by the window of the room."
        "At the same time, you can hear someone enter"
        scene black
        scene D4H
        image D4H = im.Scale ("D4H.png", 1920, 1080)
        with fade
        v "Hey..."
        m "How do you feel?"
        v "Good I think."
        v "So, how was your day?"
        m "Oh, you know, hanging out in the city, meeting some people, the usual I guess."
        v "Riiiiight..."
        scene black
        scene D4H2
        image D4H2 = im.Scale ("D4H2.png", 1920, 1080)
        with fade
        m "What about you?"
        v "Well, I wasn't allowed to join class so, I stood with Chumee and Lou."
        m "Hmm I see, that doesn't matter much, this school is a trap, we won't learn anything there."
        v "What do you mean?"
        m "I'll tell you all later, don't worry."
        scene black
        scene D4H3
        image D4H3 = im.Scale ("D4H3.png", 1920, 1080)
        with fade
        v "Hmm, anyway, We haven't been alone in a while."
        if GFVD4 == True:
            $VLove += 1
            scene black
            scene D4H4
            image D4H4 = im.Scale ("D4H4.png", 1920, 1080)
            with fade
            v "And I remember asking you for a 'small date'."
            m "Indeed, have anything in mind?"
            v "Hmm, how about we just hang out together, on my bed for now?"
            m "Sure, that sounds a bit special said like that don't you think?"
            v "Well, maybe we can have fun later if we have the time!"
            scene black
            scene D4H6
            image D4H6 = im.Scale ("D4H6.png", 1920, 1080)
            with fade
            m "Wow, jumping right into it."
            m "It's going a bit fast don't you think?"
            v "Yeah, I-I spend some time with Lou yesterday, while you were at Elise's."
            v "I know that there is something magic around her, maybe an aura that makes everything horny or stuff."
            scene black
            scene D4H7
            image D4H7 = im.Scale ("D4H7.png", 1920, 1080)
            with fade
            v "But, I don't want to fight it, I've been doing what I always wanted in the past few days, and here I am with you."
            v "Without her I would've never been able to ask you that."
            scene black
            scene D4H8
            image D4H8 = im.Scale ("D4H8.png", 1920, 1080)
            with fade
            v "Maybe it's curiosity, maybe it's because I don't know what I want for the future, but for now, I want you to feel good."
            v "And I want to feel good with you."
            scene black
            "Vanessa a bit hesitant deicide to undress, you follow her lead."
            "She's obviously shy about her body, but you can feel the lust in her eyes."
            v "I-I'm not ready yet for you to put it in."
            v "But y-you can use my thights."
            scene vid G
            v "There, just like... that..."
            m "You're really warm..."
            v "So are you..."
            "You can feel her crotch warming a little more and starting to twitch."
            v "You... you're good at this."
            v "Fuck it feels good!"
            v "I dreamed of this moment for so long."
            v "Just you, being on top of me, taking care of me..."
            v "Or am I taking care of you?"
            v "Maybe I just exist for you to use?"
            "Those words urges you to speed up!"
            scene vid H
            v "W..Wow!"
            v "Fuck!"
            "You can feel the moisture on your shaft, as you bring Vanessa's legs closer."
            v "Yeah!"
            v "Use me!"
            v "Feel good using me!"
            v "Shit! I'm so close!"
            v "P-Please!"
            v "[name]... finish with me..."
            v "Hmm!"
            with vpunch

            v "I-I'm Cuu-!!"
            v "Hmm!"
            v "Wow, you... that... I..."
            scene black
            scene Vcum
            image Vcum = im.Scale ("Vcum.png", 1920, 1080)
            with fade

            scene black
            "A few seconds after finishing, you can hear knocking at your door."
            "In a panic, Vanessa quickly dresses up, you follow her lead."
            v "That was close..."
            m "Yeah..."
            "You finally decide to open the door."

        else:
            $VLove += 1
            scene black
            scene D4H5
            image D4H5 = im.Scale ("D4H5.png", 1920, 1080)
            with fade
            m "Yeah, I missed having you around."
            v "Oh, that's sweet..."
            "You spend some time with Vanessa."
            "You finally hear someone knocking at the door, probably the others."
            "You open the door."
    scene black
    scene D4H9
    image D4H9 = im.Scale ("D4H9.png", 1920, 1080)
    with fade
    "You notice, Elise, Chumee, Lou and... Himia ?!"
    h "H-Hey, I-I thought I would join too."
    h "I still owe you both a lot after what happened."
    h "And I want to make amend."
    scene black
    scene D4H10
    image D4H10 = im.Scale ("D4H10.png", 1920, 1080)
    with fade
    "Elise slowly whispers in your ear."
    e "I discovered something related to her in the book."
    e "Having her here might be a good idea."
    menu :
        "I didn't expected her."
        "Apologize for your behaviour":
            scene black
            scene D4H12
            image D4H12 = im.Scale ("D4H12.png", 1920, 1080)
            with fade
            $SRYHD4 = True
            $HLove += 1
            $ELove += 1
            m "Listen, I'm sorry Himia for this morning, I-I was just... you know under preassure."
            m "But aiming my anger at you was not a good thing."
            scene black
            scene D4H11
            image D4H11 = im.Scale ("D4H11.png", 1920, 1080)
            with fade
            h "It's fine, I understand, I'm glad you were able to forgive me..."
        "Yeah whatever...":
            scene black
            scene D4H12
            image D4H12 = im.Scale ("D4H12.png", 1920, 1080)
            with fade
            "You look at Himia"
            "She doesn't seem as happy as before, she looks rather... sad."
            m "Whatever come in."
            h "T-Thanks."
    scene black
    scene D4H13
    image D4H13 = im.Scale ("D4H13.png", 1920, 1080)
    with fade
    "You all sit near the table."
    c "So, big guy, what was that 'important news'?"
    "You look at Elise one last time, she seem to give her approval for you to continue."
    m "Yesterday... Elise and I found a book, written by Helirios."
    scene black
    scene D4H14
    image D4H14 = im.Scale ("D4H14.png", 1920, 1080)
    with fade
    e "My father."
    h "Your father?!"
    c "Wow..."
    v "He really is your father?"
    e "Yeah he is, and we discovered an important thing, in that grimoire."
    scene black
    scene D4H15
    image D4H15 = im.Scale ("D4H15.png", 1920, 1080)
    with fade
    h "Historiene om enhet ?"
    e "What?"
    h "Means 'Tales of Unity' in english."
    e "Oh, yeah my father used smart runes that fits the reader's language."
    e "By the way what language was that?"
    h "Norwegian, my tribe spread around Iceland and Norway after the war."
    e "I see... about the war..."
    e "... That war never happened."
    scene black
    scene D4H16
    image D4H16 = im.Scale ("D4H16.png", 1920, 1080)
    with fade
    h "What do you mean?"
    e "You'll see."
    e "Close your eyes."
    scene black
    e "[name] You should check the stories we explored last night, we might expect some new pages."
    stop music fadeout 1.0
    e "And repeat after me..."
    e "Meg fra den nåværende tidslinjen, dvel i sannheten som er min."
    "All of the voices in the room seem absolutly synchronized."
    "It sounds like a calming and mystical song."
    play music "mystery.mp3"
    jump BookD4

label BookD4:
    scene black
    scene ToUBook
    image ToUBook = im.Scale ("ToUBook.jpg", 1920, 1080)
    with fade
    menu:
        "The white haired mage":
            if TaleWhiteMage == True:
                ef "I am Helirios."

            else:
                $TaleWhiteMage = True
                ef "I am Helirios."

            scene black
            ef "And if you're reliving this memory, it means my plan to preserve the truth succeeded."
            ef "***** Seems to be trying to manipulate the memories of everyone, the mad fool!"
            ef "I don't know in what kind of world I am speaking to."
            ef "But know that 'Everything is a lie'"
            ef "Either way, maybe my past will allow you to fight my battle, for I am probably dead."
            "..."
            scene black
            scene HL
            image HL = im.Scale ("HL.png", 1920, 1080)
            with fade
            ef "To fight the Armaggedon, I needed an ally."
            ef "And I got one."
            ef "Me, Magister of my people."
            ef "And Lilian, even though her origins are still a bit blurry for me."
            ef "I could always count on her, I always had her back and she always had mine."
            if ELove >= 15:
                "Your relationship with Elise has grown stronger, more about Helirios can be uncovered."
                scene black
                scene D4H17
                image D4H17 = im.Scale ("D4H17.png", 1920, 1080)
                with fade
                "You seem to distinguish a human shape in the shadows, but you can't really see who it is."
                ef "My Brother, he always was... distant, smart, kind, talented."
                ef "He got blessed by the moon after all!"
                ef "He created a lot of spells, I envy his skills sometimes."
                ef "Even though I am as powerful as him, I don't know if it will remain that way forever."
                scene black
                scene D4H18
                image D4H18 = im.Scale ("D4H18.png", 1920, 1080)
                with fade
                ef "I want Elise to learn from him too, but he has been rather distant from his niece since Elena's death."
                ef "I wonder why is he trying to dodge her."
                ef "The strings of faith..."
                ef "I'll leave that spell in the book, it's one of my creation, Manipulatin a human's mind on the short term."
                ef "That way I'll be able to occupy the guards keeping the lake, allowing me and Lilian to investigate."
                "You learned the Mind Control, at this state it can only be used to delete memories on a really short term, and reinstruct the target for basic tasks."
                $Mcontrol = True



            jump BookD4
        "The red widow." if TaleWhiteMage == True:
            $TaleRedWidow = True
            "Lou's presence reveal the image hidden behind that tale."
            scene black
            scene D4H19
            image D4H19 = im.Scale ("D4H19.png", 1920, 1080)
            with fade
            lm "Ah, the sweet kiss of the sun."
            lm "I missed it, if only Helirios could look beyond his dusty books he could see how beautiful this world is!"
            lm "'We have to study ways to preserve the world if you want to see it Lilian, think about your child's future!'"
            lm "Yeah, that's what he would say."
            scene black
            scene D4H21
            image D4H21 = im.Scale ("D4H21.png", 1920, 1080)
            with fade
            lm "But I can't blame him."
            lm "And... as a father, he's not wrong."
            if LLove >= 3:
                "Your relationship with lou growing, the name that was last time impossible to understand is now clear."
                lm "I just hope wherever he is, Marcus is safe..."

            else:
                lm "I just hope wherever he is, ***** is safe..."
                "Lilian's memories seems shattered, that one lacks a visual support."
            if LLove >= 3:
                "Your relationship with Lou has grown stronger, more about Lillian can be uncovered."
                scene black
                scene D4H20
                image D4H20 = im.Scale ("D4H20.png", 1920, 1080)
                with fade
                lm "Hmm, a good name..."
                lm "I don't know good human names!"
                lm "Ugh, I wish Marcus was here."
                lm "Well, We are close enough to France, Elise got her name from this country."
                lm "Hmm maybe I can pick one from that one too..."
                lm "Louise... But... what if it's a boy?"
                scene black
                scene D4H21
                image D4H21 = im.Scale ("D4H21.png", 1920, 1080)
                with fade
                lm "Guess I'll figure it out, I always do."

            jump BookD4
        "The Misanthrope" if LLove >= 2 and TaleRedWidow == True and HLove >= 1:
            "Lou and Himia's presence reveals a new tale!"
            mar "It's incredibly calm, it feels so magestic and yet, so primitive."
            mar "The northern tribe has proven to be really welcoming..."
            mar "They even taught me an ancient spell, Avdødes gave."
            mar "I learned it alongside two elves coming of age, Himia and her brother, Eleon."
            mar "I've been living with them for a few days now..."
            mar "Himia is always so peaceful, reading a book at the window, while Eleon is more active."
            mar "Always coming screaming at me 'Marcus, can you help me check my casting circle?'."
            mar "He seems so promising, I'm sure he will turn into a great person."
            mar "I wonder if the Unity between all races might help our world."
            mar "The goblins that I tried to contact were willing to engage in commercial actions."
            mar "I'm curious about them."
            h "MARCUS! Diner is ready!"
            mar "I'm coming!"
            "The souvenir seem to lack an image support."




            jump BookD4
        "Instructions":
            "While casting 'Avdødes gave' You've been sent through the memories of past heroes."
            "Everytime you encounter this screen you are able to visit the past."
            "Depending of your choices more paths & memories will unlock."
            "You can access the Grimoire once every day at night depending on the current event of the game."
            "Note for Day 4: New stories were uncovered depending on your choices."
            jump BookD4

        "Continue":
            jump NightD4

label NightD4:
    scene black
    scene D4H22
    image D4H22 = im.Scale ("D4H22.png", 1920, 1080)
    with fade
    h "W...What was that?"
    h "Marcus, he was a human living with us."
    h "I think I remember something..."
    l "Mother!"
    l "I can't believe it! I never thought I would see her again!"
    e "Hm Athael, my uncle."
    e "He never really took care of me."
    c "Who were these people."
    v "Yeah I...I didn't recognize any..."
    m "It's a long story... let me explain everything."
    scene black
    "You spend some time telling everyone what you saw with Elise last night."
    "The Armaggedon, and how it modified the memories of every living things."
    "Of Helirios a great magister and his friend Lilian."
    "But a tale remained blurry, Marcus's."
    scene black
    scene D4H23
    image D4H23 = im.Scale ("D4H23.png", 1920, 1080)
    with fade
    h "B-But then where is my mother?"
    h "If the human didn't took her, where is she?"
    h "W-What happened... I can't remember."
    stop music fadeout 1.0
    h "Those memories seems as true as those of the war!"
    e "Stay calm..."
    h "I-I need some time..."
    scene black
    "Himia leaves the room, you can notice her hands shaking."
    "She finally enters your room, probably out of a need to be alone."
    scene black
    scene D4H24
    image D4H24 = im.Scale ("D4H24.png", 1920, 1080)
    with fade
    m "That's my room."
    e "Well maybe you should talk to her..."
    m "You're right."
    scene black
    "You stand up, and walk slowly into your room."
    "In your room, you notice Himia in tears sat on your bad."
    "You sit next to her."
    scene black
    scene D4H25
    image D4H25 = im.Scale ("D4H25.png", 1920, 1080)
    with fade
    play music "blind.mp3"
    m "You know, I remember that war too, as if it happened a few days ago."
    m "And yet, since those revelations I feel like there is more."
    scene black
    scene D4H26
    image D4H26 = im.Scale ("D4H26.png", 1920, 1080)
    with fade
    h "It feels so real, and yet I remember Marcus, I can't deny the truth your grimoire brings!"
    h "But... I need some time, my brother too lives in this lie."
    h "God and he attacked Vanessa..."
    scene black
    scene D4H28
    image D4H28 = im.Scale ("D4H28.png", 1920, 1080)
    with fade
    h "I hope he will realise that all of this might be a lie..."
    m "I hope too..."

    menu:

        "Let's return with the group.":
            m "Let's return with the group, they all have been through the same thing."
            scene black
            scene D4H28
            image D4H28 = im.Scale ("D4H28.png", 1920, 1080)
            with fade
            h "You...You're right."
            scene black
            "You take Himia's hand helping her standing, she's taller than you expected."
            "And you lead her back to everyone."
            e "We all learn difficult things Himia, but now you got us, and even though your brother is... well what he is."
            e "He is a victim as well."
            h "Thanks... Elise I appreciate it."
            jump Night2D4
        "Let's spend some time together":
            $HLove += 2
            m "Here let's spend some time alone, far from the noise."
            scene black
            scene D4H27
            image D4H27 = im.Scale ("D4H27.png", 1920, 1080)
            with fade
            h "Yeah that's a good idea, I could use some time thinking about something else."
            if HLove >= 4:
                scene black
                scene D4H28
                image D4H28 = im.Scale ("D4H28.png", 1920, 1080)
                with fade

                h "You know, my tribe had a lot of good history about ancient magics, we were one of the oldest tribe."
                h "The ice elves we were called, or the snow elves."
                h "I just came of age when Marcus the first human joined us to learn about our culture."
                m "Came of age?"
                scene black
                scene D4H29
                image D4H29 = im.Scale ("D4H29.png", 1920, 1080)
                with fade
                h "Yeah, I recieved a ceremony and a mark near... well the lowest part of my belly."
                m "Oh, I wonder how it looks like!"
                scene black
                scene D4H30
                image D4H30 = im.Scale ("D4H30.png", 1920, 1080)
                with fade
                h "It's a bit personnal, but I guess I can show it to you, I don't mind it."
                scene black
                "Humia slowly takes of her clothes keeping only her underwear on."
                scene black
                scene D4H31
                image D4H31 = im.Scale ("D4H31.png", 1920, 1080)
                with fade
                m "Wow I didn't expect you to take everything off!"
                h "Well, I did!"
                h "How does it look?"
                m "Lovely."
                m "Actually your entire body is."
                h "Oh, that's sweet, thanks..."
                h "..."
                scene black
                scene D4H34
                image D4H34 = im.Scale ("D4H34.png", 1920, 1080)
                with fade
                h "Do you want to see more?"
                h "that way you might be able to fully see it."
                m "I'd love to."
                scene black
                "The elf takes a deep breath, and finally takes her last pieces of clothes off."
                scene black
                scene D4H32
                image D4H32 = im.Scale ("D4H32.png", 1920, 1080)
                with fade
                h "There, I do like my curves honestly!"
                m "And you're right to like em', you look amazing!"
                h "Oh than-"
                with hpunch
                "*Knock Knock*"
                scene black
                scene D4H33
                image D4H33 = im.Scale ("D4H33.png", 1920, 1080)
                with fade
                l "Are you alright in there?"
                scene black
                "In a move of panic Himia quickly dresses back up."
                m "Y-Yeah don't worry, we're coming out!"
                h "{size=-10} Next time, you show me yours! {/size}"
                jump Night2D4
            else:
                h "Yeah, I'd like that..."
                scene black
                "You spend some time with Himia."
                "She talks to you once more about books."
                "She seem so passioned by them that she quickly smiles."
                "You finally both head back to the living room, you feel your bond with her growing stronger."
                jump Night2D4


    label Night2D4:
        "As the time passes, the sun slowly set."
        "Leaving the stage for the bright light of the moon."
        stop music fadeout 1.0
        scene black
        scene D4H38
        image D4H38 = im.Scale ("D4H38.png", 1920, 1080)
        with fade
        e "It's getting awfully late!"
        play music "rain.mp3"
        c "Yeah, I should get home."
        scene black
        scene D4H35
        image D4H35 = im.Scale ("D4H35.png", 1920, 1080)
        with fade
        v "Hmm, how about you all stay here for the night?"
        v "We all head to the academy tomorrow anyway..."
        scene black
        scene D4H36
        image D4H36 = im.Scale ("D4H36.png", 1920, 1080)
        with fade
        v "Except [name]... of course."
        e "Well, that sounds good to me!"
        c "Why not!"
        scene black
        scene D4H37
        image D4H37 = im.Scale ("D4H37.png", 1920, 1080)
        with fade
        v "What about you Himia?"
        h "Sure I'd love to know more about all of you!"
        h "by the way..."
        scene black
        scene D4H39
        image D4H39 = im.Scale ("D4H39.png", 1920, 1080)
        with fade
        h "Seems like you got quite acustomed to manipulating the mana, [name]!"
        m "Indeed, I wonder if I'll be able to make my own spells at one point."
        m "Might be hard since the academy decided that human didn't had any rights on anything magic related!"
        scene black
        scene D4H40
        image D4H40 = im.Scale ("D4H40.png", 1920, 1080)
        with fade
        e "We can teach you and Vanessa of course!"
        v "You would do that?"
        e "Of course I would!"
        e "I'm not the daughter of a Magister to never use my spells!"
        scene black
        scene D4H41
        image D4H41 = im.Scale ("D4H41.png", 1920, 1080)
        with fade
        c "I just hope you two won't turn into lazy persons by using magic at every occasion!"
        m "We won't, I just want to know the truth about what happened twenty years ago."
        m "My first dream led me to 30 years ago, when the humans met the elves for the first time."
        m "And it seems like the books hold the memories of what happened ten years later."
        c "Dreams?"
        m "I've been having dreams about the past for a while now."
        l "Wow, that's worrying."
        l "I hope you know I can't do anything about them though."
        m "I know, anyway, let's just talk about something else!"
        stop music fadeout 1.0
        scene black
        "You spend the evening with the girls."
        "The ambiance feels, calm, friendly, warm, sort of like a family."
        "But you all slowly fall asleep, using the spell once again drained you all of your energy."

        play music "mystery2.mp3"
        scene black
        scene D4DR
        image D4DR = im.Scale ("D4DR.png", 1920, 1080)
        with fade
        ef "Hmm, Lillian!"
        lm "Yeah, yeah I'm coming..."
        scene black
        scene D4DR1
        image D4DR1 = im.Scale ("D4DR1.png", 1920, 1080)
        with fade
        ef "It seems like a magic circle was drawn here, not too long ago."
        lm "Hmm, and what can you say about that circle."
        ef "It still a bit weak, but I can feel the power of the moon, the blood, and fire."
        lm "Just that, well."
        ef "Quit being sassy, it's serious, usually the moon cannot be crossed with the fire, and blood magic is usually used in Sacrifices."
        lm "So, you're suggesting a sacrifice happened here?"
        scene black
        scene D4DR2
        image D4DR2 = im.Scale ("D4DR2.png", 1920, 1080)
        with fade
        ef "Precisely, but who would be sacrificed, and why?"
        ef "Sacrifices have been forbidden since forever!"
        ef "Although there are but few users of the power of the moon in the ancient tribe nowdays, most of them moved out to the northern tribe, or the Southern tribes."
        ef "I should ask my brother, he needs to know what happened here using his the power of the moon."
        scene black
        "Helirios copies the runes used for the spell on a piece of paper, before putting it in one of his pocket."
        scene black
        scene D4DR3
        image D4DR3 = im.Scale ("D4DR3.png", 1920, 1080)
        with fade
        lm "You're using paper?"
        lm "Why don't you use a spell to copy it."
        ef "I can't risk losing it, the elves are too proud to use paper, they would never suspect me for using such 'barbaric' methods."
        lm "Fair enough."
        ef "Come on let's get back to Elise, I've got a spell to teach her after all!"
        lm "Oh I didn't knew you were that much of a loving father!"
        scene black
        scene D4DR4
        image D4DR4 = im.Scale ("D4DR4.png", 1920, 1080)
        with fade
        ef "I might not be the best father, but I want the best for my little sun."
        scene black
        lm "You're a good person nerd."
        stop music fadeout 2.0
        ef "I try to be."
        "..."
        play music "rain.mp3"
        "You can hear a voice in the distance..."
        "The sound of the rain slowly joins it, it's relaxing, and yet... Oppressive."
        "It's slightly rocky, and yet young, neither scary nor reassuring."
        vhead "Ah... it took some time."
        vhead "But I'm finally alone in there."
        m "Who said that?"
        m "Lou is that you?"
        vhead "Come on... do I really sound like a girl?"
        m "Well you don't sound at all actually, probably because it's tex-"
        vhead "Cut it out for a second..."
        vhead "Where was I?"
        vhead "Oh right, that succubus is finally out there."
        m "Come on, my head isn't some kind of hellish hotel, who are you?"
        vhead "Oh, no my boy, I'm not exactly in your head, I'm just talking through it."
        vhead "As for my identity, well... you'll know it in time, let's go for a walk you and I..."
        "You can feel your soul slowly leaving your body..."
        vhead "Soo, [name]..."
        vhead "A few days ago, you told me..."
        if PeaceD1 == True:
            vhead "That this world deserves peace, do you still live by that statement?"
            menu :

                "Yes":
                    vhead "Oooh, I see."
                    vhead "What about Eleon, he tried to kill your friend!"
                    vhead "Are you not afraid he could come in, and finish the job tomorrow?"
                    vhead "After all..."
                    if AngerD4 == True:
                        vhead "You tried to fight back, you showed will to kill."
                        vhead "Curious..."
                    else:
                        vhead "You did tried to save your friend, you ended a cycle to save the injured..."

                "No":
                    vhead "Oooh, I see."
                    $PeaceD1 = False
        else:
            vhead "That this world didn't deserve peace, that it was... a dream!"
            vhead "Do you still live by that statement?"
            menu :

                "Yes":
                    vhead "Ah! I see."
                    vhead "After all, Eleon tried to hurt your loved ones!"
                    vhead "I understand your pain human."
                    if AngerD4 == True:
                        vhead "And yet I don't understand, how can you be so encline to deny peace's existence, if you're hurt by the loss of a friend?"
                        vhead "After all, death happens in wars!"
                        vhead "But it seems you understood that when you tried to fight back that elf."

                "No":
                    $PeaceD1 = True
                    vhead "Oh!"
                    vhead "So even though you didn't believed in peace at all..."
                    vhead "even though an elf tried to kill your kind..."
                    vhead "even though the principal punished you for a crime you didn't commit, and didn't punished someone trying to murder your close ones."
                    vhead "You're still ready to forgive them."
                    if AngerD4 == True:
                        vhead "But then, why did you try to kill, to make that elf boy pay?"
                        vhead "You call for peace when it suits you..."

        vhead "Either way!"
        vhead "This proved terribly... interesting."
        vhead "Be careful human, the cult is after you."
        vhead "And your friends, soon you will have to hide."
        vhead "I can't control them anymore."
        vhead "Prove your worth, and I shall reward you, your friends."
        m "Wait, who are you?"
        vhead "Call me... the arbiter."
        arbiter "This is all a trick, that book has a lot of layers, keep following it."
        arbiter "When you're ready, follow Elise's call, she should remember something tomorrow..."
        stop music fadeout 1.0
        "The voice slowly dissapear, you can feel your soul being called back to your body."
        play music "FilledLove.mp3"

        scene black
        scene D5M1
        image D5M1 = im.Scale ("D5M1.png", 1920, 1080)
        with fade
        l "Yesterday was great!"
        l "We should do it again some time!"
        c "Yeah it was nice!"
        v "I'm sure we'll be able to spend another night together!"
        l "Hot."
        scene D5M2
        image D5M2 = im.Scale ("D5M2.png", 1920, 1080)
        v "I-I didn't meant like that!"
        l "I know, I know, I'm messing with you..."
        scene D5M3
        image D5M3 = im.Scale ("D5M3.png", 1920, 1080)
        m "By the way Lou, how did the academy allowed you to join?"
        m "I remember spending quite some time with Vanessa to be allowed to join it."
        l "I didn't."
        m "Wait so why are you here?"
        l "I look like any human here."
        l "Honestly the first day was a pure hit or miss!"
        l "And apparently the administration didn't gave enough of a damn to take me out so, y'know."
        scene D5M4
        image D5M4 = im.Scale ("D5M4.png", 1920, 1080)
        e "Either way we won't learn much here."
        e "And here I expected to learn some new spells, and way to see things."
        m "I mean, you don't strike me as a girl that needs more training."
        e "Oh that's nice, but you know, every day is a new lesson!"
        scene D5M5
        image D5M5 = im.Scale ("D5M5.png", 1920, 1080)
        h "Hmm, I-I should get to my brother, him and I have a lot to talk."
        m "Sure, just avoid what we saw yesterday... for now."
        h "Don't worry."
        scene D5M6
        image D5M6 = im.Scale ("D5M6.png", 1920, 1080)
        m "And you Vanessa, are you not worried about what happened yesterday?"
        v "Oh, I am, but you know, Himia is here, so is Elise, and the nurse was really nice to me yesterday."
        v "She asked me if I wanted to learn some healing spells with her."
        m "Wow, I thought no one here would teach human anything."
        v "Well, she's really curious about our relationship to mana, maybe her thirst for knowledge goes beyond that."
        v "Beside, I'm also part of 'the plan'"
        scene black
        "Vanessa and the girls leave you alone with Elise waving their hands at you."
        "Except Elise."
        scene D5M7
        image D5M7 = im.Scale ("D5M7.png", 1920, 1080)
        m "The plan?"
        e "The plan indeed, [name] the principal has my mother's dress, it bugs me a lot to ask that much of you, but I need you to steal it back."
        with vpunch
        m "WHAT?"
        m "How, I'm pretty sure she could dissolve me in a second!"
        scene D5M8
        image D5M8 = im.Scale ("D5M8.png", 1920, 1080)
        e "Don't be silly, I wouldn't let you there without any assurance."
        if ELove >= 15:
            e "Beside what would I become without MY primate?"

        e "Remember when I teached you how to lit a flame with your finger?"
        scene D5M9
        image D5M9 = im.Scale ("D5M9.png", 1920, 1080)
        e "Now you will direct the mana in an object, the principal's door."
        e "Elisandre will be with Delphine and Vanessa for the whole morning, she will close the door, but you will enter, take the dress, and join me here once you're done."
        m "What exactly am I supposed to do?"
        e "Just touch the handle of the door, and flow some mana through it, of course, it's probably warded!"
        e "But the elves here don't expect a human to tresspass, they all think you guys are powerless."
        e "The door cannot be opened with a key, so you know, just give it a good ol' mana flow!"
        m "Wow, I'm not used to you using that accent!"
        scene D5M10
        image D5M10 = im.Scale ("D5M10.png", 1920, 1080)
        e "Ahem, me too."
        e "Alright meet me back here once you're done!"
        m "Wait, wait, the dress might be quite tall, how am I supposed to hide it?"
        e "Just wear it."
        with hpunch
        m "WHAT?!"
        scene D5M11
        image D5M11 = im.Scale ("D5M11.png", 1920, 1080)
        e "I'm joking! Gods, if you could see your face!"
        scene D5M12
        image D5M12 = im.Scale ("D5M12.png", 1920, 1080)
        e "Just think about the dress being doll-sized."
        e "It will adjust to the size you think about."
        m "Oh, weird, but okay."
        e "See you later, and please be careful!"
        m "I will."
        scene D5M13
        image D5M13 = im.Scale ("D5M13.png", 1920, 1080)
        with fade
        ukn "..."
        scene black
        with fade
        "You wait for the courtyard to finally be empty..."
        "Once you're sure no one is in sight, you enter the academy."
        "You would have expected some magic shield to protect the academy from intruders."
        "That doesn't seem to be the case."
        "You quietly get to the last floor, where the Principal's office is located."
        scene black
        m "Hmm..."
        scene D5M14
        image D5M14 = im.Scale ("D5M14.png", 1920, 1080)
        with fade
        "You touch the door for a bit."
        "Nothing. It seems ordinary, but you do notice the absence of a doorknob."
        "As you begin charging your hand with Mana, you can feel someone staring at you..."
        ukn "Hello."
        "You can feel your blood stopping in your veins, as you slowly turn around."
        scene D5M15
        image D5M15 = im.Scale ("D5M15.png", 1920, 1080)
        with fade
        with vpunch
        ukn "You want me to help you get in?"
        m "Damn, you scared me!"
        m "Who are you, why would you help me?"
        ukn "I'm Valoria, I heard you wanted to get back something the principal stole."
        m "Wait, you eavesdropped back in the courtyard?"
        Val "I did."
        m "And  you would believe us, without any proof?"
        Val "That elf girl protected a human yesterday."
        Val "She said that no more innocent had to suffer because of pride."
        Val "A person with a noble goal cannot act like that without good reasons."
        Val "I can help you with the door, unless you don't want me to."
        m "(She does have a point, but should I really trust her?)"
        menu :

            "Let Valoria help":
                $ValoriaHelpD5 = True
                scene D5M18
                image D5M18 = im.Scale ("D5M18.png", 1920, 1080)
                with fade
                m "Alright, how can you help."
                Val "The door indeed needs to be overflowed with Mana."
                Val "But not at any place, if you overflow the wrong place, the door will open."
                Val "But the principal will notice someone broke in."
                Val "I'll look for the weak point, once I got it overflow it."
                m "I see, it makes sense, but how do you know that?"
                Val "I just know it."
                m "(Weird.)"
                scene black
                "The girl puts her hands on the door, with an elegant flow to it."
                "As if she was dancing with the mana... of a Door."
                "It feels extremely weird, but also gracious as absurd as it sounds."
                "You don't feel the air moving, she's not moving, and yet it feels like it."
                "How can a human girl control the mana that well?"
                Val "I got it."
                "She takes of her hand off the door."
                scene D5M19
                image D5M19 = im.Scale ("D5M19.png", 1920, 1080)
                Val "Overflow this point, not too much just enough to open it."
                $OverflowD5 = True
                "You follow the girl's lead, at first it's a bit hard to feel the mana, but after a few second, you manage to open the door."
                m "It worked!"
                m "Thanks Valoria!"
                Val "Glad I was able to help."
                Val "I'm sure we'll meet again [name]."
                "The Grey haired girl silently moves out, leaving a strange atmosphere."
            "Do it alone":
                scene D5M16
                image D5M16 = im.Scale ("D5M15.png", 1920, 1080)
                with fade
                m "Thanks, but I think I'll be alright."
                Val "Hmm, your call, good luck."
                m "Yeah, thanks..."
                Val "You should be careful about where you overflow the door."
                scene D5M17
                image D5M17 = im.Scale ("D5M17.png", 1920, 1080)
                with fade
                m "... Weird."
                "You focus on the door, take a deep breath, although you notice a small point in the door, empty of all mana."
                menu :

                    "Overflow the empty spot":
                        $OverflowD5 = True
                        scene black
                        "You take a deep breath, and focus your energy in the small empty part."
                        "It's the true Doorknob, the energy goes through the door and flows back in the floor, although a major point is open."
                        "Filling it should allow the mana to go through."
                        "It worked!"
                        "The door opens itself slowly and silently."
                    "Just overflow the door":
                        scene black
                        "You focus the mana in your palm, and conduct it on the door."
                        "The door opens itself in a tantrum."
                        m "(SHIT!)"
                        with hpunch
                        "You quickly get inside and close the door behind you."
        scene D5M20
        image D5M20 = im.Scale ("D5M20.png", 1920, 1080)
        with fade
        "Nothing changed from Yesterday."
        "Your eyes wipe the room, nothing."
        scene black
        m "Guess I will have to look deeper."
        "You check more closely everything especially the office, and you notice a very small form."
        m "The dress!"
        "As you touch it, you immediately got an image of Elise wearing it in your mind."
        "The dress instantly take Elise's proportion, it indeed is hers."
        "You follow Elise's instructions as you imagine it at a portable size and hide it in your pocket."
        "There is nothing left to do in the room."
        stop music fadeout 1.0
        "You open the door, and calmly close it behind you."
        "Time to check on Elise at the main gate and give her the dress."
        scene black
        "As you look at the hall, your blood freezes."
        scene D5M21
        image D5M21 = im.Scale ("D5M21.png", 1920, 1080)
        with fade
        play sound "HBeat.mp3"
        m "(What is he doing here!?)"
        m "(He was supposed to be in class!)"
        "Before being able to do anything, the elf's eyes found you."
        scene D5M22
        image D5M22 = im.Scale ("D5M22.png", 1920, 1080)
        with fade
        Ele "YOU!"
        with vpunch
        Ele "What are you doing here!"
        Ele "No matter, no one will save you now!"
        Ele "I'll end you here and now, and when people will know you disobeyed the principal's orders."
        Ele "They will realize that your specie is worth nothing and you'll go back at our knees!"
        m "(Fucking son of a bitch, I have to do something!)"
        m "(I can fight him, but either way it's risky, he might be stronger or I can beat the shit out of him.)"
        m "(Although I can't really say if Himia will be pleased, nor if the consequences will be... acceptable.)"
        m "(I can try to reason with him, yesterday I learned sensible informations, and I feel like the situation is an urgency.)"
        if Mcontrol == True:
            m "(Or I can mind control him, make him forget what he was doing here and that he saw me!)"
        menu :

            "Mind control him" if Mcontrol == True:
                "This action will have consequences."
                play music "Blind.mp3"
                m "(Sounds like the best choice.)"
                m "By the sun, thy light brings me knowledge."
                m "By the moon, thy darkness brings me conviction."
                m "By the stars, thy guidance will prove me right in the mind of the doubtful!"
                scene D5M23
                image D5M23 = im.Scale ("D5M23.png", 1920, 1080)
                with fade
                Ele "Wh-"
                Ele "..."
                m "(Did it worked?!)"
                m "Eleon."
                scene D5M24
                image D5M24 = im.Scale ("D5M24.png", 1920, 1080)
                with fade
                Ele "Yes, sir."
                m "You will forget about everything you saw, you will forget about me, and of course you will forget what is happening right now."
                m "You will act as if you never saw me."
                Ele "Yes sir."
                m "Oh and Eleon..."
                m "Don't lay, a fucking hand on Vanessa or my friends, or anyone that doesn't deserve it ever again."
                Ele "Y-Yes sir."
                m "(Yikes, it's really weird to use it on a male.)"
                m "(But it's done.)"
                scene black
                "You go down the stairs knowing that you did the right thing."
            "Fight him":
                "This action will have consequences."
                $Elefight = True
                m "It's time for some payback you pointy ear'd bastard!"
                "No spells, just your bare hands, close and personal."
                "He won't expect it."
                Ele "Oh, oh, you're approaching me?"
                "As you run against him, his ice shard seems to be deviated, you notice as you run that a magic shield covers you."
                "Yet you don't remember using any spell."
                scene D5M31
                image D5M31 = im.Scale ("D5M31.png", 1920, 1080)
                with vpunch
                Ele "WHAT?!"
                with vpunch
                Ele "You can't just deflect the Emerald Spl-..."
                Ele "My ice shard!"
                m "I can't beat the shit out of you without getting closer."
                Ele "No! GET AWAY FROM ME!"
                scene D5M25
                image D5M25 = im.Scale ("D5M25.png", 1920, 1080)
                with vpunch
                Ele "How?"
                scene pele5
                with hpunch
                m "I won't let you hurt anyone else!"
                scene black
                "Eleon instantly falls to the ground and lose conciousness."
                "Something felt odd about your strength, as if you used magic without knowing it."
                scene D5M26
                image D5M26 = im.Scale ("D5M26.png", 1920, 1080)
                with fade
                "His nose seems to be bleeding, nothing beyond that."
                m "So much for a noble and proud elf."
                m "With a bit of luck you will forget what happened."
                scene black
                "You get down the stairs, leaving the elf unconcious on the ground."
            "Convince him" if VLove >= 10 and HLove >= 5:
                "This action will have consequences."
                $EleKnow = True
                play music "Blind.mp3"
                m "Marcus and Himia wouldn't approve that!"
                Ele "I am protecting my Sister, you won't hurt her!"
                m "What about Marcus, you remember in the northern tribe, the human that learned with you!"
                Ele "Wh-"
                Ele "Marcus? I-I-I..."
                Ele "Wait."
                Ele "Marcus."
                Ele "I think I..."
                Ele "Yes, I think we learned something together..."
                Ele "Wait... me and a human..."
                scene D5M28
                image D5M28 = im.Scale ("D5M28.png", 1920, 1080)
                with fade
                Ele "What is going on! What have you done to me!"
                m "Nothing, and I won't do anything."
                m "I care about your sister, as much as I care about my friend."
                m "I don't want you to hurt them."
                scene D5M29
                image D5M29 = im.Scale ("D5M29.png", 1920, 1080)
                with fade
                Ele "B-but you are inferor..."
                m "Then why did you learn alongside one of us?"
                m "Aren't we Equal?!"
                Ele "Aaaah! I-I need time."
                Ele "F..fine go, I won't tell..."
                m "Thank you."
                scene D5M30
                image D5M30 = im.Scale ("D5M30.png", 1920, 1080)
                with fade
                Ele "Just..."
                Ele "Please, I want my sister to be happy, I don't want her to suffer."
                m "Trust me, me too."
                scene black
                "You leave silently."
                m "(Hmm, he surrendered really quickly, I didn't expect it to be that easy.)"
                m "(But why...)"
                m "(His mind probably got twisted into reality, and the spell, I'll have to mention that to Elise & Himia."
                Ele "What is happening, why am I so kind! He's a human they did horrible things!"
                Ele "I need to rest, I feel dizzy."
        stop music fadeout 1.0
        m "Hm..."
        m "I could check on Chumee or the infirmary before heading to the courtyard..."
        play music "blackbird.mp3"
        menu:

            "Check on Chumee":
                $CLove += 2
                m "(Hmm, Chumee is always at the tracking field, she probably is still there.)"
                "You make your way to the tracking field, where you indeed meet Chumee and her sisters."
                scene D5C1
                image D5C1 = im.Scale ("D5C1.png", 1920, 1080)
                with fade
                mh "Oh hey!"
                scene D5C2
                image D5C2 = im.Scale ("D5C2.png", 1920, 1080)
                with fade
                c "[name], You're not supposed to be here!"
                mh "Oh, you could be grateful Chumee, look at the risk he takes to just see you!"
                c "Hmm..."
                scene D5C3
                image D5C3 = im.Scale ("D5C3.png", 1920, 1080)
                with fade
                m "Wanted to check up on you before going."
                mh "How cute, come Dai' let's leave them both alone."
                dai "Sure."
                if CLove >= 8 and CVirginity == True:
                    scene D5C4
                    image D5C4 = im.Scale ("D5C4.png", 1920, 1080)
                    with fade
                    c "Well, if you're up for a risk, how about a quicky in the storage room!"
                    m "You know it."
                    c "That's why I like you."
                    scene black
                    "Chumee leads you to the storage room, it's a bit dark, but nothing too dramatic."
                    c "I've been waiting since last time!"
                    c "I missed that big shaft of yours!"
                    c "Come on, [name], take me!"
                    scene vid cd5
                    c "Hm!"
                    c "Th-that's what I needed!"
                    c "Nothing compares to that feeling!"
                    c "Keep going!"
                    c "A-Ah!"
                    scene vid cd52
                    c "Shit! I didn't knew you could go faster!"
                    c "What the fuck! How does it feel so good?!"
                    c "You better fill me up, I want you to breed me!"
                    c "I-I'm so close, finish in me, finish WITH me..."
                    scene black
                    c "FUUUCK!"
                    scene cpsd5
                    with fade
                    c "T-That was a bit loud, but... Shit that..."
                    c "That was insane."
                    m "Were you serious about the breed thing?"
                    scene cpsd52
                    c "Oh uh... were you serious about breeding me?"
                    menu :

                        "Yeah":
                            $CLove += 2
                            scene cpsd5
                            m "Yeah."
                            c "Well yeah, I was."
                            m "I liked it."
                            c "Then I might stop taking these pills."
                        "No":
                            m "Not really no."
                            c "O-Of course I was joking."
                            c "You know, heat of the passion and stuff."
                            m "Yeah I get."
                    c "You should meet Elise outside, I'll just take a small break here."
                    m "Yeah, sure see you later!"
                    scene cpsd53
                    c "Bye handsome!"
                    jump EliseGate

                else:
                    "You spend some time with Chumee, you feel your bond with her growing bigger."
                    $CLove += 3
                    jump EliseGate
            "Check the infirmary":
                $VLove += 1
                $LLove += 1
                m "(Lou is probably with Vanessa at the infirmary, although the principal is there I think I'll wait for a bit and check on them.)"
                "You make your way near the infirmary wait a bit to be sure that the principal leave, and get in."
                scene D5I1
                image D5I1 = im.Scale ("D5I1.png", 1920, 1080)
                with fade
                v "Oh [name]!"
                l "What are you doing here?"
                doc "Oh, [name], you indeed shouldn't be here!"
                m "I wanted to make sure everything was alright."
                doc "Hm, I don't know why you're here but you better stay inside for now."
                doc "Beside, I'm still waiting for those samples!"
                scene D5I2
                image D5I2 = im.Scale ("D5I2.png", 1920, 1080)
                with fade
                l "Hmm..."
                v "Well I'll go back to class with Lou, see you later [name]!"
                l "Yeah..."
                scene black
                "Before leaving lou whispers slowly in your ear..."
                l "Have fun..."
                "You can feel the room getting slightly hotter."
                scene D5I3
                image D5I3 = im.Scale ("D5I3.png", 1920, 1080)
                with fade
                doc "Hmm, so... those samples."
                m "Yeah, what do you need me to do?"
                doc "Just undress, I'm done having jars of hair or spit, I want to have fun too..."
                m "(That was raw.)"
                doc "I'm sooo... lonely, I haven't touched someone else in years."
                doc "Those research take most of my time, so if I can have fun while working, I won't refuse it."
                doc "Sit down I'll pump those 'samples' out of you..."
                scene black
                "You obey, and sit on one of the bed as the nurse locks the room."
                scene vid DI1
                doc "Let me take care of you now..."
                "You can feel Delphine's hot breath on your shaft, as she slowly pumps you."
                "She's very delicate, very seductive."
                doc "Your friends are so lucky... Having you around, I'm sure they all fantasize about getting knocked up by you..."
                doc "I wish I could get rid of that bitch of a principal."
                doc "I would gladly take you back here, and take care of you every day."
                scene vid DI2
                doc "I'm done playing, now I want you to mess my face with your juices!"
                "The doc goes faster, she definitely knows what she's doing."
                doc "I can feel you're close!"
                doc "finish on my face!"
                doc "I want to feel your human seeds against my skin!"
                scene dcumd5
                with fade
                doc "YES!!"
                with vpunch
                scene black
                doc "That was... nice."
                doc "You should leave, before someone catches you."
                "Like a rogue you follow her advice, wave at her and head to the gate silently."

                jump EliseGate

            "Just get to the gate":
                jump EliseGate








    label EliseGate:
        stop music fadeout 1.0
        "Elise is still waiting for her dress."
        "Now that you're done here you join here in front of the academy."
        scene ed5
        e "[name]! I was worried."
        m "You shouldn't be."
        play music "Blackbird.mp3"
        "You hand over the dress, Elise take a good look at it, before having a smile slowly being drawn on her face."
        "She hides it in one of her pocket."
        scene ed51
        e "Gods, I thought I would never see it again."
        e "Thank you [name]!"
        e "Really."
        if ELove >= 15:
            scene ed52
            $ELove += 1
            "Elise jumps at your neck and holds you close to her."
            e "I'll thank you proprely later."
        scene ed51
        e "I should get going but I'll see you later!"
        m "Sure thing."
        scene black
        "You look at Elise going back in the academy as you wait against a wall, wondering how you could spend your day."
        "As you're about to go home, you recognzie a familiar voice."
        scene mod5
        o "Oh [name]!"
        m "Ophelia, Mine?"
        mi "How are you?"
        m "I guess I'm doing alright, what about you two?"
        scene mod51
        o "You know, the usual, I'll hang out at the beach with Mine today, want to join us?"
        m "(I really don't have anything else to do, perhaps I should join them)"
        m "Yeah, sure."
        mi "Great, let's go!"
        "You follow Ophelia & Mine, the road is really quiet."
        "Finally you three get at the beach, it's empty."
        scene D5B
        image D5B = im.Scale ("D5B.png", 1920, 1080)
        with fade
        o "Hm, no one, good."
        o "Let's take a seat and change clothes, I'm exhausted!"
        "You three take a seat on the shore."
        scene D5B2
        image D5B2 = im.Scale ("D5B2.png", 1920, 1080)
        with fade
        o "Ah! It's been a while!"
        m "Since you've been at a beach?"
        o "Yeah..."
        m "When was the last time?"
        scene D5B3
        image D5B3 = im.Scale ("D5B3.png", 1920, 1080)
        with fade
        o "Hm... I was 4, with my parents, a few days before the war ended and humans were reduced to slavery."
        m "Oh..."
        scene D5B4
        image D5B4 = im.Scale ("D5B4.png", 1920, 1080)
        with fade
        mi "Let's not talk about this Ophe, you know I don't like seeing you like that..."
        o "You're right Kitty, we're here to relax for a bit."
        scene D5B2
        image D5B2 = im.Scale ("D5B2.png", 1920, 1080)
        with fade
        o "And you [name], how do you fare?"
        m "Hmm, nothing special, since I'm out of the academy I have nothing else to do, a shame I would've loved to learn some spells."
        o "You can learn them without the academy you know?"
        m "Well, how?"
        scene D5B5
        image D5B5 = im.Scale ("D5B5.png", 1920, 1080)
        with fade
        o "Experiment, elves think humans can't harness magic, but we can if you know how to feel the mana currents, you can experiment."
        o "Of course, the bigger the spell is, the more training you need."
        stop music fadeout 1.5
        m "How did you learn all of that?"
        scene D5B6
        image D5B6 = im.Scale ("D5B6.png", 1920, 1080)
        with fade

        o "W-Well... When I was younger, I had a huge potential mana wise."
        o "I could harness great spells while I was really ... young."
        scene D5B7
        image D5B7 = im.Scale ("D5B7.png", 1920, 1080)
        with fade
        m "It was near the war, how did the elves react?"
        o "... Bad... Really badly, they took me."
        scene D5B8
        image D5B8 = im.Scale ("D5B8.png", 1920, 1080)
        with fade
        o "T-Took my parents."
        o "They, they experimented on me."
        scene D5B9
        image D5B9 = im.Scale ("D5B9.png", 1920, 1080)
        with fade
        o "I remember... the shock, the pain, my musles being twisted, my bones broken."
        o "I was... I was..."
        with hpunch
        scene D5B3
        image D5B3 = im.Scale ("D5B3.png", 1920, 1080)
        with fade
        mi "Enough Ophe!"
        mi "We'll tell him when you feel ready, alright?"
        o "Yo-You're right, sorry."
        mi "Good, for now let's relax."
        play music "blackbird.mp3"
        m "You're right Mine, I could go for a swim."
        scene D5B10
        image D5B10 = im.Scale ("D5B10.png", 1920, 1080)
        mi "I-In the water?"
        m "Well yeah, oh right, you're a cat."
        scene D5B11
        image D5B11 = im.Scale ("D5B11.png", 1920, 1080)
        with fade
        mi "I-I'm a woman! I can perfectly swim too!"
        o "Oh really? I'm really curious about the way you swim then!"
        scene black
        mi "W-well, I'll show you, come [name]."
        mi "..."
        scene D5B12
        image D5B12 = im.Scale ("D5B12.png", 1920, 1080)
        with fade
        mi "Soo... I-I don't really know how to swim, and the water is cold, I think I-I'll just stay near Ophe..."
        m "Come on, I can help you, I'll just keep you against me so you don't drown."
        mi "That sounds... Good."
        scene black
        "As you and mine slowly leave a bit the shore she puts her hands on your neck holding you close."
        scene D5B13
        image D5B13 = im.Scale ("D5B13.png", 1920, 1080)
        with fade
        mi "Oh G-god how can you stay calm?"
        m "It's just water, it can't arm neither of us."
        mi "But but you get all wet, and the current is so strong!"
        m "Well water is wet, can't do much about it."
        m "As for the current you just need to swim and be careful."
        scene D5B14
        image D5B14 = im.Scale ("D5B14.png", 1920, 1080)
        with fade
        mi "I never learned how to swim."
        m "Well I teached a friend a few days ago..."
        scene D5B15
        image D5B15 = im.Scale ("D5B15.png", 1920, 1080)
        with fade
        mi "Really? You would teach me?"
        m "Well yeah I guess!"
        scene D5B16
        image D5B16 = im.Scale ("D5B16.png", 1920, 1080)
        with fade
        mi "Thank you! But... For now, can we just stay like that for now?"
        mi "It feels nice, and you're warm."
        m "Whatever you want."
        scene black
        "Mine's breath is soft and warm agains your shoulders, you can feel her slowly resting against you, breathing calmly, it's... relaxing."
        m "Come on, let's get back to Ophelia."
        scene D5B17
        image D5B17 = im.Scale ("D5B17.png", 1920, 1080)
        with fade
        mi "Yeah we should, and [name]..."
        mi "You're really are comfy."
        m "... I just noticed, but since you changed, you lost your ears."
        scene d5b18

        with fade
        mi "Oh, yeah I can hide them, it's quite useful when I come to public places."
        m "But we're alone."
        mi "I don't want any sand or water inside, it's way harder to take it out."
        m "Now that you mention it, it must be annoying."
        scene black
        "You get back to the shore, where Ophelia is."
        scene d5b19
        o "Seeing you two hugging for ten minutes was adorable!"
        o "When do I get a turn?"
        menu :

            "Soon enough":
                scene d5b20
                o "Careful now, I might expect more than that!"
                $OLove += 1
            "Another time":
                scene d5b21
                o "What a shame."
        scene d5b22
        mi "Say [name]!"
        mi "We talked about Ophelia earlier, but where did you grow up?"
        o "I'm curious too, we don't know that much about you."
        scene d5b23
        m "Hm, I don't remember much my first years of being alive, the 'war' began a bit before my birth."
        m "Some people apparently gave me to a woman living in the countryside in the US."
        m "There I grew up with a friend, I remember the crops, the fresh air of the countryside."
        m "There, the elves didn't come, they mainly controlled cities, so we lived freely."
        m "I don't really remember my parents, I just remember them being taken away."
        m "And a beach, a beach I used to visit, when I was younger."
        m "Before I joined my friend and her mother of course."
        m "I heard a lot about Ophelia, but Mine, I'm convinced you were not human before, what happened?"
        scene d5b24
        mi "Hmm..."
        mi "It's a long story, probably a bit bloody."
        o "Mine, keep it simple, he doesn't need the details if you don't want him to know yet."
        mi "Yeah, I know."
        mi "I was born out of necromancy."
        m "Necromancy ?!"
        with vpunch
        scene d5b25
        o "Exactly, Necromancy, a forbidden type of magic using the dead."
        m "But, How, how is it possible?"
        scene d5b26
        mi "I was born from..."
        mi "From..."
        scene d5b27
        mi "I-I can't, I'm sorry it's just..."
        o "You know [name], Mine and I got a specal story, it's really complicated to... talk about it, that freely."
        o "Anyway, I'd like to avoid that subject for now."
        m "I understand."
        o "Good, I expected you to run out at the first occasion when you heard 'necromancy', glad you didn't."
        "You lay down on the sand, it's warm, it feels like a cloud, a really dusty cloud."
        scene d5b28
        with fade
        mi "[name]?"
        m "Yeah?"
        mi "Do you have a mate?"
        m "Uh..."
        o "Come on Mine, that redhead elf is probably already his mate, or maybe that childhood friend."
        o "Or Perhaps Himia, you have a lot of girls around you [name]."
        mi "I'm sure they wouldn't mind having me around!"
        scene d5b29
        m "..."
        o "Hmm, Perhaps, but if they don't mind I want to hop in too!"
        "You notice Ophelia's smug smile, she knows what she's doing."
        mi "I don't mind, but I want to be his favorite!"
        o "Oh, Kitty you have a lot of people to reccon with then!"

        mi "..."
        scene d5b30
        with fade
        with vpunch
        m "(what.)"
        o "(what.)"
        mi "I heard, males love to see them, what do you think [name]?"
        menu :

            "I love them!":
                scene d5b31
                $MLove += 1
                mi "I'm glad you like em', you want to touch them?"
                o "..."
                scene d5b33
                with vpunch
                o "I'm sure he prefers mine."
                o "Cop a feel."
            "I've seen better.":
                scene d5b32
                mi "Oh..."
                o "..."
                scene d5b33
                with vpunch
                o "Perhaps you would prefer mine!"
                o "You can touch them go ahead!"
                mi "Wait, then he can touch mine!"
        scene d5b34
        m "I'm so glad to be alive."
        m "(Mine's are small and perky, they're adorable...)"
        m "(While Ophelia's are way bigger, and feels soft...)"
        menu :

            "I prefer Mine's":
                $MLove += 1
                mi "See? I told you he would like them!"
                o "Seems like you prefer small sizes, a shame."
            "I prefer Ophelia's":
                $OLove += 1
                o "See? He prefers mine!"
                mi "Awh..., I wish my chest was as big as yours!"
            "I love both of them." if MLove >= 2 and OLove >= 2:
                $MLove += 1
                $OLove += 1
                o "Come on that's the easy way."
                mi "Can't you make a choice."
                m "No, I love them both, they have their own little 'thing'."
                o "You're lucky you're that handsome."
        scene d5b35
        with fade
        o "That was fun, but we should head home Mine."
        mi "Oh already?"
        o "Yeah kitty! The sun is almost setting!"
        m "Wow, time flies, I too should head home."
        scene d5b36
        o "It was nice seeing you again [name], have a good one!"
        mi "Bye!"
        stop music fadeout 1.0
        $OLove += 2
        $MLove += 2
        scene black
        "You put back your clothes and head home."
        "There you just lay on your bed, and close your eyes."
        scene dreamd5arbiter
        with fade
        arbiter "So, you got the dress?"
        play music "mystery2.mp3"
        m "You again?"
        arbiter "What do you mean?"
        m "Well, Can you just let me get some rest for a while?"
        scene dreamd5arbiter2
        arbiter "You'll rest when you'll die, beside if you don't pay attention, it might come sooner than expected!"
        m "What do you mean?"
        scene dreamd5arbiter
        arbiter "The cult knows, it knows that you can use magic, it knows that you have the Tales of Unity."
        arbiter "It knows that you met the experiment and her feline friend."
        arbiter "In a few days they might act."
        m "What am I supposed to do?"
        scene dreamd5arbiter2
        arbiter "The Dwarven Kingdoms."
        m "The Dwarven kingdoms?"
        scene dreamd5arbiter
        arbiter "Indeed, dwarves and elves have always been in conflict, when the war ended, the Dwarves got back to their own kingdom, high in the mountains or deep beneath the earth."
        arbiter "There would be a nice place to escape."
        m "But I don't know exactly where it is."
        scene dreamd5arbiter3
        arbiter "Well, just look for infos, I don't know, I'm just a voice in your head!"
        arbiter "Before I leave you to rest, do you have any questions?"
        jump QuestionAD5

    label QuestionAD5:

        menu :

            "What cult?":
                scene dreamd5arbiter2
                arbiter "The cult of the stars, some elves maniacs that mainly controls everything that happens within their reach."
                m "How do you know about them?"
                arbiter "I'm closer to them than you would suspect."
                jump QuestionAD5
            "Why me?":
                scene dreamd5arbiter
                arbiter "You're in the middle of many species, Goblins, elves, monsters, demons."
                arbiter "You're a good subject to study."
                arbiter "But don't feel like an object please, I study everything, but in the current context, it is important for me to see what is happening."
                jump QuestionAD5
            "What are you?":
                scene dreamd5arbiter2
                arbiter "I'm... alive, I'm nothing but in love with this world, the trees, the birds, the air, everything."
                arbiter "And I want to preserve this beautiful world."
                arbiter "I am a living being, perhaps I'm a dwarf, or an elf, a human, or Joe mama."
                m "Who's J-"
                arbiter "Anyway."
                jump QuestionAD5
            "What are those visions I have at night?":
                scene dreamd5arbiter3
                arbiter "The visions from Helirios are not part of the book, they're part of the Armaggeddon."
                arbiter "They're scattered bits of memory that got in contact with your mind."
                arbiter "You should pay attention to them, some holds important informations, and you might be able to learn new things."
                jump QuestionAD5
            "What do you look like":
                scene dreamd5arbiter3
                arbiter "Haha! You'd like to know don't you?"
                scene dreamd5
                arbiter "I can look like anyone, Helirios."
                scene dreamd52
                arbiter "Eleon."
                arbiter "Or I don't know... YOU?!"
                scene dreamd53
                arbiter "Oh come on! Now that's a convienient way to hide your face."
                arbiter "Hiding it behind shadows, it feels like some cartoonish censor."
                arbiter "Anyway, you get it!"
                m "But you had an appearance before changing, close to Helirios."
                arbiter "Well maybe I'm an elf, and I was a magister so I wear magister clothes?"
                arbiter "I'm unrelated to him."
                jump QuestionAD5
            "Continue":
                arbiter "Anyway, I've helped you enough."
                arbiter "This has been interesting to say the least."
                arbiter "You won't see me for a while."

    scene d5o
    P "Hmm..."
    P "I'm pretty sure the dress was here!"
    ukn "This dress belonged to the traitor's wife, and his daughter."
    ukn "How could you lose something that valuable!"
    scene d5o2
    P "I-I, somebody must've stolen it!"
    ukn "And who? Who could've known it was here!"
    P "I-I Maybe the daughter's traitor, Elise!"
    ukn "How would she know?"
    scene d5o3
    P "She's a witch, a traitor, and her human friend probably came in and stole it for her!"
    ukn "Isn't your door protected?"
    scene d5o4
    if OverflowD5 == True:
        P "I-It is, but I didn't felt anything special while opening the door!"
        ukn "So whoever took it, knew how to overflow a door, it might be an elf..."
    else:
        P "I did noticed huge cracks in the flow of the door!"
        ukn "So it might be a human indeed."
    ukn "Either way, taking care of them won't be easy."
    ukn "We will keep an eye on that human [name], and his friend Elise, actually, we'll keep an eye on their whole party."
    scene d5o5
    P "Good, something is odd about them."
    ukn "We heard the Tale of Unity might be in your establishement again."
    P "I heard these rumors, but I looked for it, I even checked when the Traitor's daughter was alone in the library this morning, Nothing!"
    ukn "Then his daughter is useless."
    ukn "We can't let humans know about the truth, they would learn our ways, learn about magic and could reverse everything!"
    ukn "That's a lot of coincidence, first you lose the robe, then the Tales of Unity leaves your establishment."
    ukn "Helirios hid the book alongside his work, only a member from his bloodline could reveal it, if it didn't appear, then it's already gone."
    ukn "The cult is on it's way, We'll take care of them once we're here."
    ukn "We all suffered enough during the war because of these humans, and finally, we will be able to take direct actions."
    ukn "We can finally move forward, we need to eliminate that traitor and her friends, they might've read the book already."
    ukn "You will be our sword while we act, gather informations, kill anyone in your way."
    scene d5o6
    P "... I am honored."
    P "Let me take care of the girl, her father's treachery cost the life of my husband, I demand retribution."
    ukn "..."
    ukn "Fine, but you will act when told, we don't need the citizens to know that we violated our only rule."
    P "No elves turn on the others, she's no elf, she's a traitor."
    ukn "...We will speak again shortly."
    scene black
    P "So be it."
    stop music fadeout 1.0
    "You didn't have any dream while resting."
    "It was calm, peaceful, you didn't felt that much relief in a whi-"
    scene d5lr
    with dissolve
    l "Oh, you're awake, a shame, I thought I could have fun with you."
    play music "FilledLove.mp3"
    menu :

        "We can":
            $LLove += 2
            scene d5lr2
            with fade
            l "I knew you were the fun type, come on sit down!"
            scene black
            m "Is it your first time doing it?"
            l "Well yeah, I've spend the rest of my time in your head!"
            m "Aren't you a bit scared or something?"
            l "Why would I be, there is nothing more pure than sex, it's the best way people found to express their love."
            m "So we're a couple?"
            l "Haha, no, no we're far more than that, you and I shared a mind."
            l "Within you, I feel something familiar, I care about you as much as I care about me, you're like a part of me."
            l "And I'm a part of you."
            m "Sounds wholesome."
            l "Don't get used to it, I still want you to fuck me silly."
            m "Well now it sounds like selfcest."
            m "Buuuut..."
            m "I can do that..."
            l "Come on, get in!"
            scene vid loud5
            l "Hmm~"
            l "You fit right in~"
            l "You know, you're quite handsome, I had a good host."
            l "You're good..."
            l "But I feel like you could do better!"
            l "How about you TRULY take me."
            scene vid loud52
            l "W-Wow!"
            l "Fuck!"
            l "Holy shit, that's good!"
            l "Don't stop, you better not fucking stop!"
            l "How can it be so good?!"
            l "You like fucking my tight hole?"
            l "You like using me?"
            l "Fuck I'm losing it, finish inside!"
            scene loucumd5
            with vpunch
            l "Yyyyeeees!"
            with vpunch
            l "Fuck, you don't mess around..."
            l "You filled me up good..."
            scene black
            "You both take some time to get back on your feet."
            "Lou seems satisfied if not glad that you accepted her offer."

        "Yeah, no":
            scene d5lr3
            l "Meh, you're not fun!"

    l "Anyway..."
    if ELove >= 16:
        scene d5l
        l "Elise asked to see you, she's at the new hot spring that opened a few days ago."
        m "A hot spring?"
        l "Yeah a story about a date or something, Himia is with her she apparently has a few words for you."
        m "(shit, that has to be about her brother.)"
        l "Anyway, I'll just stay here, do, you know, succubus stuff."
        m "Whatever little demon!"

    else:
        scene d5l
        l "Himia wanted to talk to you, she's at the new hot spring."
        m "She told you what she wanted?"
        l "Not really, she's just there, Elise is with her."
        m "Alright I should go then."

    scene d5l2
    with fade
    "You put your hand on Lou's head."
    m "Tell Vanessa I'll come back late."
    l "Yeah sure!"
    l "See ya'"

    scene black
    stop music fadeout 1.0
    "You cross the doorstep, and head to the new hot spring."
    "It opened a few days ago at the edge of the city."
    "After a few minutes of walking alone, your gaze Finally meet Elise's."
    "Next to her is Himia."
    play music "blackbird.mp3"
    scene d5ss
    e "Hey [name]!"
    e "I hope the day wasn't too boring!"
    m "No, no it was quite alright."
    e "Good, I was about to head to the hot spring, but Himia wanted to talk to you."
    m "Really? About what?"
    h "My brother."
    m "(Shit.)"
    if Elefight == True:
        scene d5ssfight
        h "He came to me, a few minutes after your departure, his nose was bleeding."
        h "You did this to him, right?"
        m "I didn't have any choice!"
        scene d5ssfight2
        h "You did! You could've told him the truth, he would've backed off!"
        m "You don't know that, he could've killed me there, could've told the principal, could've got the human back to slavery since 'they can't behave'."
        h "I still think you could've avoided it!"
        m "No, it was inevitable, I taught him a lesson."
        scene d5ssfight
        h "Whatever."
        h "I hope it was worth it at least."
        m "It was."
        jump EliseBookD5


    elif EleKnow:
        scene d5ssknow
        h "He came to me, telling me about a human."
        h "Marcus."
        h "What happened up there?"
        m "I had to tell him the truth, I didn't wanted to hurt him."
        m "You told me he isn't evil, I trust you."
        scene d5ssknow2
        h "Thank you, seriously, I'll remember that!"
        h "Anyway, I just wanted to say that."
        if HLove >= 5 and ELove <= 15:
            h "Also, perhaps, you'd like to come with me and gaze at the stars for a bit, I'd like some company."
            menu :

                "I'd love to":
                    $ELove += 1
                    h "Amazing!"
                    e "Well, have a good evening, I'll get in for a bit, I could use some hot water."
                    h "Bye Elise!"
                    m "See you tomorrow!"
                    jump HimiaDate
                "Refuse":
                    scene d5ssrefuse
                    h "What a shame..."
                    h "Maybe another time then!"
                    jump EliseBookD5
        else:
            jump EliseBookD5
    else:
        scene d5ssknow2
        h "I wanted to thank you for our talk yesterday."
        m "Oh, no worries, glad to be of service."
        if HLove >= 5 and ELove <= 15:
            h "Also, perhaps, you'd like to come with me and gaze at the stars for a bit, I'd like some company."
            menu :

                "I'd love to":
                    $ELove += 1
                    h "Amazing!"
                    e "Well, have a good evening, I'll get in for a bit, I could use some hot water."
                    h "Bye Elise!"
                    m "See you tomorrow!"
                    jump HimiaDate
                "Refuse":
                    scene d5ssrefuse
                    h "What a shame..."
                    h "Maybe another time then!"
                    jump EliseBookD5


    label EliseBookD5:
        h "Anyway, I should get going, have a good one you two."
        e "Bye Himia!"
        m "See you tomorrow!"
        scene d5ev
        e "Hmm, [name], I also wanted to tell you, I granted you access to the grimoire on your own."
        m "What do you mean."
        e "From now on, you won't need to have the grimoire near you to check it."
        e "I would still advise using it at night, since it drains you of your energy."
        m "Alright, thanks Elise!"
        scene d5ev2
        e "No worries."
        if ELove >= 16:
            scene d5ev3
            e "I do remember promising a reward, come on let's get in!"
            e "Unless of course, you would prefer to go home."
            menu :

                "How can I deny that?":
                    e "You can't!"
                    jump HotSpringD5
                "I'm a bit exhausted":
                    e "Oh, I see, that's a shame but I understand, see you tomorrow, sweet dreams!"
                    m "You too Elise."
                    scene black
                    "You finally head home."
                    "There you notice Vanessa & Lou sleeping, you follow their exemple and head to bed too."
                    jump Dreamd5


        else:
            e "You should get going, I took enough of your time, see you tomorrow!"
            m "Bye!"
            scene black
            "You finally head home."
            "There you notice Vanessa & Lou sleeping, you follow their exemple and head to bed too."
            jump Dreamd5








    label HotSpringD5:
        scene black
        with dissolve
        "The night slowly embraces the sky as you dip in the hot water with Elise."
        "It's calm and relaxing."
        scene d5hs
        with fade
        e "I needed that..."
        m "Me too, so much has happened!"
        scene d5hs2
        e "Yeah, but now we've got an objective, and I'm sure we'll be able to figure out everything that's going on!"
        e "..."
        scene d5hs3
        e "It's beautiful... isn't it, the sky."
        scene d5hs4
        with fade
        m "It is."
        scene d5hs3
        with fade

        e "My tribe always placed it's destiny within the stars."
        e "For us, each great elf turns into a star that joins the immortal sky."
        m "That's poetic."
        scene d5hs5
        e "Cliché is more the word, but... I do like the idea of having my mother and my father watching over me."
        scene d5hs6
        e "I wanted... to give you something else, for you know... what you did for me."
        m "Oh really? What kind of thing?"
        e "Y-You know, you, me, We both want it."
        e "I just don't... feel ready yet."
        e "I know I want my first to be you, but I'm still not ready to take that step..."
        menu :

            "I understand":
                scene d5hs7
                with fade
                $ELove += 1
                m "We'll wait until you're ready."
                m "For you, I don't mind."
                e "Thanks, it means a lot."
            "That's a shame":
                e "I know I'm sorry..."
        e "..."
        m "..."
        scene d5hs3
        e "I remember having a house with my father in our small Island."
        e "We both used to flee there when the guards became annoying, it was, our little corner."
        m "Perhaps we will be able to see it again!"
        scene d5hs5
        e "definitely!"
        e "Hmm, my father might have hidden some hints there too, although..."
        scene d5hs8
        e "I can't remember where it is precisely."
        e "Damn spell, I still don't know why I was spared by the big part of the Armaggeddon though."
        m "That's something we'll figure out together."
        m "For now, we both earned some rest."
        scene d5hs2
        e "Yeah, no grimoire tonight, I know I gave you access to it, but perhaps you should take a break."
        m "We got your dress this morning, it belonged to your mother, and it felt weird when I got it in my hands."
        stop music fadeout 1.0
        m "I want to know more, I'm sure the book holds more about it."
        scene d5hs8
        e "Hmm, Alright, let's give it a look right now then."
        play music "rain.mp3"
        jump BookD5

        label BookD5:
            scene black
            scene ToUBook
            image ToUBook = im.Scale ("ToUBook.jpg", 1920, 1080)
            with fade
            menu:
                "The white haired mage":
                    if TaleWhiteMage == True:
                        ef "I am Helirios."

                    else:
                        $TaleWhiteMage = True
                        ef "I am Helirios."

                    scene black
                    ef "And if you're reliving this memory, it means my plan to preserve the truth succeeded."
                    ef "***** Seems to be trying to manipulate the memories of everyone, the mad fool!"
                    ef "I don't know in what kind of world I am speaking to."
                    ef "But know that 'Everything is a lie'"
                    ef "Either way, maybe my past will allow you to fight my battle, for I am probably dead."
                    "..."
                    scene black
                    scene HL
                    image HL = im.Scale ("HL.png", 1920, 1080)
                    with fade
                    ef "To fight the Armaggedon, I needed an ally."
                    ef "And I got one."
                    ef "Me, Magister of my people."
                    ef "And Lilian, even though her origins are still a bit blurry for me."
                    ef "I could always count on her, I always had her back and she always had mine."
                    if ELove >= 15:
                        scene black
                        scene D4H17
                        image D4H17 = im.Scale ("D4H17.png", 1920, 1080)
                        with fade
                        "You seem to distinguish a human shape in the shadows, but you can't really see who it is."
                        ef "My Brother, he always was... distant, smart, kind, talented."
                        ef "He got blessed by the moon after all!"
                        ef "He created a lot of spells, I envy his skills sometimes."
                        ef "Even though I am as powerful as him, I don't know if it will remain that way forever."
                        scene black
                        scene D4H18
                        image D4H18 = im.Scale ("D4H18.png", 1920, 1080)
                        with fade
                        ef "I want Elise to learn from him too, but he has been rather distant from his niece since Elena's death."
                        ef "I wonder why is he trying to dodge her."
                        ef "The strings of faith..."
                        ef "I'll leave that spell in the book, it's one of my creation, Manipulatin a human's mind on the short term."
                        ef "That way I'll be able to occupy the guards keeping the lake, allowing me and Lilian to investigate."
                        "You learned the Mind Control, at this state it can only be used to delete memories on a really short term, and reinstruct the target for basic tasks."
                        $Mcontrol = True



                    jump BookD5
                "The red widow." if TaleWhiteMage == True:
                    $TaleRedWidow = True
                    "Lou's presence reveal the image hidden behind that tale."
                    scene black
                    scene D4H19
                    image D4H19 = im.Scale ("D4H19.png", 1920, 1080)
                    with fade
                    lm "Ah, the sweet kiss of the sun."
                    lm "I missed it, if only Helirios could look beyond his dusty books he could see how beautiful this world is!"
                    lm "'We have to study ways to preserve the world if you want to see it Lilian, think about your child's future!'"
                    lm "Yeah, that's what he would say."
                    scene black
                    scene D4H21
                    image D4H21 = im.Scale ("D4H21.png", 1920, 1080)
                    with fade
                    lm "But I can't blame him."
                    lm "And... as a father, he's not wrong."
                    if LLove >= 3:
                        "Your relationship with lou growing, the name that was last time impossible to understand is now clear."
                        lm "I just hope wherever he is, Marcus is safe..."

                    else:
                        lm "I just hope wherever he is, ***** is safe..."
                        "Lilian's memories seems shattered, that one lacks a visual support."
                    if LLove >= 3:
                        "Your relationship with Lou has grown stronger, more about Lillian can be uncovered."
                        scene black
                        scene D4H20
                        image D4H20 = im.Scale ("D4H20.png", 1920, 1080)
                        with fade
                        lm "Hmm, a good name..."
                        lm "I don't know good human names!"
                        lm "Ugh, I wish Marcus was here."
                        lm "Well, We are close enough to France, Elise got her name from this country."
                        lm "Hmm maybe I can pick one from that one too..."
                        lm "Louise... But... what if it's a boy?"
                        scene black
                        scene D4H21
                        image D4H21 = im.Scale ("D4H21.png", 1920, 1080)
                        with fade
                        lm "Guess I'll figure it out, I always do."

                    jump BookD5
                "The Misanthrope" if LLove >= 2 and TaleRedWidow == True and HLove >= 1:
                    if EleKnow == True:
                        "Telling Eleon the truth uncovered a new part of the tale."
                    elif Elefight == True:
                        "Being violent against Eleon closed the opportunity to learn more about the Misantrope for now, you can still read what you already uncovered."
                    else:
                        "Controlling Eleon's mind uncovered a part of the tale."

                    mar "It's incredibly calm, it feels so magestic and yet, so primitive."
                    mar "The northern tribe has proven to be really welcoming..."
                    mar "They even taught me an ancient spell, Avdødes gave."
                    mar "I learned it alongside two elves coming of age, Himia and her brother, Eleon."
                    mar "I've been living with them for a few days now..."
                    mar "Himia is always so peaceful, reading a book at the window, while Eleon is more active."
                    mar "Always coming screaming at me 'Marcus, can you help me check my casting circle?'."
                    mar "He seems so promising, I'm sure he will turn into a great person."
                    mar "I wonder if the Unity between all races might help our world."
                    mar "The goblins that I tried to contact were willing to engage in commercial actions."
                    mar "I'm curious about them."
                    h "MARCUS! Diner is ready!"
                    mar "I'm coming!"
                    if EleKnow == True:
                        h "So, Eleon you learned something new?"
                        Ele "I did! I managed to go back through time, I saw through our grand parents eyes!"
                        mar "Seems like you already got used to your ancestral spell kid."
                        Ele "Seems like it, I'm curious, have you tried using the spell yourself?"
                        mar "I did, I tried to relive my wife's memories, she's well, way older than me."
                        Ele "You're married?"
                        h "Way older, I didn't know you were into old ladies Marcus."
                        mar "What? No, no I meant litteraly, she's not really human."
                        h "Is she an Elf?"
                        mar "Not really, a story for another time!"
                        Ele "You always tease us!"
                        mar "Damn right I do, now come on I'm hungry!"
                    "The souvenir still seem to lack an image support."
                    if Elefight == true:
                            jump BookD5

                    else:
                        h "So, Eleon you learned something new?"
                        Ele "I did! I managed to go back through time, I saw through our grand parents eyes!"
                        mar "Seems like you already got used to your ancestral spell kid."
                        Ele "Seems like it, I'm curious, have you tried using the spell yourself?"
                        mar "I did, I tried to relive my wife's memories, she's well, way older than me."
                        Ele "You're married?"
                        h "Way older, I didn't know you were into old ladies Marcus."
                        mar "What? No, no I meant litteraly, she's not really human."
                        h "Is she an Elf."
                        mar "Not really, a story for another time!"
                        Ele "You always tease us!"
                        mar "Damn right I do, now come on I'm hungry!"
                        "The souvenir still seem to lack an image support."
                        jump BookD5

                "Elena." if ELove >= 16:
                    $ElenaBook = True
                    "Elise's love towards you allowed you to uncover a new part of the book."
                    ef "My Elena, you mean everything to me."
                    ef "You blessed me, you gave me a beautiful daughter, new dreams."
                    ef "Your death... is probably the biggest loss I could think of."
                    ef "But you left me something, a hint."
                    ef "My hero, you reading through these lines, listening to my voice."
                    ef "I left a part of me inside the book, a part of my powers, this chapter is still encrypted as I try to decode the book."
                    ef "This grimoire doesn't belong to me, it belonged to my wife."
                    ef "She his within these lines, important messages that needs to be decoded, but it seems like I need more."
                    ef "My daughter Elise might be the key, I noticed runes of blood in the first pages, perhaps, once she's ready she'll be able to discover what her mother hid from us."
                    ef "Tell... Tell my daughter I love her, she's my own little start in the sky, and I'll be sure to keep my eyes on her from the skies."
                    ef "If you read these lines, you got the dress."
                    ef "Cherish it, for it is all I have left from my love."
                    "The page ends here, but there is far more to encover."




                    jump BookD5
                "Instructions":
                    "While casting 'Avdødes gave' You've been sent through the memories of past heroes."
                    "Everytime you encounter this screen you are able to visit the past."
                    "Depending of your choices more paths & memories will unlock."
                    "You can access the Grimoire once every day at night depending on the current event of the game."
                    "Note for Day 4: New stories were uncovered depending on your choices."
                    jump BookD5

                "Continue":
                    if ELove >= 16:
                        jump EliseSpringD5
                    elif HLove >= 5 and ELove <= 15:
                        jump HimiaDate2

    label EliseSpringD5:
        scene d5hs9
        e "Wow..."
        e "That's a lot to take in!"
        m "It is..."
        e "I'll have to relive these memories to be sure I understood everything correctly."
        if ElenaBook == True:
            scene d5hs6
            e "I'm glad that my mother left us something."
            e "I don't remember much of her."
            scene d5hs10
            with fade
        e "Anwyay, let's relax together for a bit, I'm done with these stories of conflict, and conspiracy, I just want to relax with the man I love for a bit."
        m "You're right little sun."
        m "I too could use some rest."
        scene black
        stop music fadeout 1.0
        "You spend the rest of the evening with Elise, you leave the hot spring as the moon slowly rises."
        "Once home, you notice Vanessa and Lou already sleeping, you follow their exemple and head to bed."
        jump Dreamd5

    label HimiaDate:
        scene d5hs11
        e "Before you go [name]..."
        e "I granted you access to the grimoire on your own."
        m "What do you mean."
        e "From now on, you won't need to have the grimoire near you to check it."
        e "I would still advise using it at night, since it drains you of your energy."
        m "Alright, thanks Elise!"
        h "Come on let's go!"
        scene black
        e "See you two lovebirds tomorrow!"
        h "bye!"
        "You walk calmly alongside Himia, the sun is slowly setting, as you finally reach your destination."
        "A small plot of grass near a lake."
        play music "surreal.mp3"
        scene d5h
        h "I use to come here when I'm exhausted, or a bit fed up."
        h "No noise, just the water flowing..."
        h "It's also a great place to read."
        m "So, how is human literature?"
        scene d5h2
        h "Oh you're taking me by the feelings with that questions."
        h "It's fantastic, all these different stories your specie managed to make, some based on facts, others on pure fiction."
        h "Creativity, diversity, you humans are unique."
        m "What do you mean?"
        h "Well you're all different, the spectrum of thoughts, idea, physique is very wide, it's interesting."
        h "Elves are not that diverse."
        m "I do think you're fairly different from the others."
        scene d5h3
        h "How?"
        m "Well, first off you didn't try to kill me... yet."
        scene d5h4
        h "haha, that's a good one, but be careful, perhaps I want to take you in another way!"
        m "How exactly?"
        scene d5h6
        with fade
        m "...!"
        "Himia sticks her soft lips against yours, you feel her warm breath against you."
        scene d5h7
        h "That is one way for an instance."
        m "I like that way a lot."
        h "Well, that's good because I like that way a lot too!"
        h "..."
        scene d5h8
        with fade
        h "I still can't believe all that changed since I met you."
        h "Learning that my memories were changed is... sometimes troubling."
        h "But I definitely remember Marcus, perhaps we should use the grimoire again!"
        m "Why?"
        scene d5h10
        h "Well... Elise told you you had an access any time."
        stop music fadeout 1.0
        m "Well, let's give it a shot then."
        jump BookD5

    label HimiaDate2:
        scene d5h10
        h "Hmm..."
        h "That was really short, but I do remember that moment, at the table, with Marcus and Eleon."
        h "I-I need time to think about what we just saw."
        m "Don't worry, we have plenty of time."
        scene d5h9
        h "Good."
        scene black
        stop music fadeout 1.0
        "You spend the evening with Himia, her feelings for you are growing."
        "As the night set, you get back home, Lou and Vanessa seem to be already asleep."
        "You follow their exemple and head to bed as well."

        jump Dreamd5

    label Dreamd5:

        play music "forgiven.mp3"
        ath "Hmm..."
        scene dd51
        with dissolve
        ath "And you're sure you saw a rune of the moon?"
        ef "I did."
        ath "That's worrying, blood runes are always aligned with sacrifices, and loss."
        ath "Why would anyone use the rune of the moon in that context?"
        scene dd52
        ef "I thought you would know."
        ath "No, I don't, it's a sacrifice to the moon, that much is obvious, it's coupled with a rune of fire, which is close to the sun."
        ath "So, perhaps a sacrifice to the stars directly."
        ef "That's worrying, sacrifices are needed for huge spells, is a cult hiding within us?"
        ath "Probably, I'll investigate on my side."
        ef "Alone, again?"
        scene dd53
        ath "...Yes."
        ef "Elise, why are you avoiding her?"
        ath "I'm not."
        scene dd54
        ef "Yes you are, she feels guilty because you've been avoiding her since her mother's death!"
        ath "I-I..."
        ef "Teach her something, she could learn from you!"
        ath "... I'll try."
        ef "You know, one day, You will have to tell me why you don't want to see your niece."
        scene dd55
        ath "It's not against her... it's more complex."
        ef "How is it more complex?!"
        ath "She's Elena's daughter! That's the issue!"
        ef "What about it?"
        ath "Please... Don't make me talk about that, You know I had feelings for her too."
        ef "..."
        scene dd56
        ath "I cared Heli', and I still do, and I'm glad you were here for her, I know you're a good father to your daughter."
        ath "I'm just, not like you, we're imperfect creatures."
        scene dd57
        with fade
        lm "Hey Heli, I heard you two shouting from the other side of the plaza, is everything alright?"
        ef "Yeah, don't worry."
        ath "Everything is fine."
        ef "Come on Lilian, let's go, be careful Athael."
        scene dd58
        ath "You too."
        ef "And never forget, we're flesh and blood, your family, and I love you as a brother should."
        ath "Thanks, me too."
        scene dd59
        lm "Get a room and work it out."
        ath "Yikes, you don't miss one Lil'."
        lm "By the way, why are your ears normal, aren't you supposed to have knife ears Athael?"
        ath "Meh, I resize them, I hate having them partly in my hood, and partly outside like my brother."
        lm "Oh I see, so Helirios is the one piercing holes here..."
        ef "As always, you're the funniest here Lilian, alright, let's go."

        scene black
        lm "Alright alright, guess your bromance is already over."
        ef "It only started in your twisted brain."

        "As the moon sets on the field."
        "The sun rises over the crops."
        "One brings shadow, one brings the light."
        "An imperfect cycle, that holds the balance."
        "One brother born under the night."
        "One under the sun."
        "Which one of them holds the mercy?"
        "Which one of them holds the retribution?"
        "Drown in the Ether plan and you shall discover the truth."

        scene ntease
        with dissolve
        ukn "..."
        ukn "*sigh*"

        scene black

        scene v05tease
        with Fade(1.0, 0.0, 2.0)


        scene black
        with Fade(0.5, 0.0, 0.5)

        ukn "We are around the city Elisandre."
        scene v05tease5
        with Fade(0.5, 0.0, 0.5)
        ukn "We found the human, he's with the experiment and it's felin monster."
        ukn "Get rid of the traitor's daughter and her friends here."
        "..."
        scene v05tease6
        with Fade(0.5, 0.0, 0.5)
        P "It shall be done as you wish."
        P "Elise will die before the sunset."
        ukn "Good, the cult will contact you once the human is dead."
        P "..."
        scene v05tease2
        with Fade(0.5, 0.0, 0.5)
        P "Delphine, bring Elise to my office."
        doc "Is something wrong?"
        scene v05tease3
        P "No, dear, everything is..."
        scene v05tease4
        stop music fadeout 1.0
        P "Absolutly fine."
        doc "I'll send her to your office right away then."
        scene black

        v "Hm... Elise?"
        scene d6m
        with fade
        play music "FilledLove.mp3"
        e "Yes?"
        v "So... I remember you telling us that you would train us."
        e "Yeah, I do remember!"
        v "Is there any spell that you could teach me?"
        scene d6m2
        e "Hmmm..."
        scene d6m3
        c "Come on, I'm curious, I've never seen Vanessa use a spell!"
        l "I thought you hated magic."
        c "I don't, I just hate the lazy people using it!"
        e "Uh, rude."
        scene d6m4
        c "Come on, just teach her!"
        scene d6m5
        e "Well, there is a small auto defense spell, something as basic as throwing a fireball."
        v "Oooh!"
        e "Same as [name]! Close your eyes!"
        scene d6m6
        l "By the way where is he?"
        v "He is with friends he met a few days ago, apparently a girl wearing cat ears, and a blonde girl."
        c "A cat girl?"
        v "Yeah."
        h "Sounds weird, but that reminds me of those mangas I read the other day!"
        scene d6m7
        l "Don't be a weeb please Himi'"
        h "A wee-"
        e "Alright, can we go back to the spell?"
        scene d6m8
        c "Party pooper..."
        l "Why is it always boring around her..."
        h "What's a weeb?"
        e "..."
        scene d6m9
        e "I'm not boring, I can be really funny and cool when I want it!"
        c "Oh really?"
        e "Well yeah!"
        c "Prove it!"
        scene d6m10
        e "Well, what's the difference between a dwarf, and a goblin?"
        h "OH! I know that one!"
        c "Uh, the color?"
        scene d6m11
        with dissolve
        e "No! The beard!"
        h "Gods, I love those jokes!"
        e "I know! They're amazing!"
        scene d6m12
        c "Uh..."
        scene d6m13
        with dissolve
        l "ha..haha yeah, amazing..."
        v "Uh... can we get back on the spell?"
        e "Of course!"
        scene d6m14
        e "Focus on the your breathing, you just need to feel the mana once, to truly manipulate it."
        e "Once you got it, follow my voice and send it to me."
        scene black
        with dissolve
        stop music fadeout 1.0
        v "Like... hitting you?"
        e "No haha, no... like throwing a snowball for an instance, or a ball of course you won't throw a ball at your ennemies but for that exemple, do as if we were playing!"
        "Vanessa takes a few seconds, long seconds to feel what's around her."
        "She can feel the fabric on her skin, warming her."
        "The fresh morning air going through her nose, to her throat, ending their course in her lungs."
        "The sound of her breathing, peace."
        v "... Hmph!"
        with vpunch
        "The flow of mana takes the form of a projectile, with a purple-ish light, going at an impressive speed."
        scene d6m15
        with flashbulb
        l "WOW! Are you ok Elise?"
        with vpunch
        c "That was insane! You got her good"
        e "Shit, that's a strong one!"
        scene d6m16
        with dissolve
        v "Oh god I'm sorry Elise, I didn't mean to hurt you!"
        e "It's alright, I've took worst in my life, beside I managed to stop it!"
        scene d6m17
        with dissolve
        e "I'm impressed I expected way less, but perhaps you have a lot more to hide!"
        v "Really? Shite..."
        scene d6m18
        c "*giggles* 'Shite'"
        scene d6m19
        play music "FilledLove.mp3"
        v "Well what can I say, I grew up in Scotland with my mother!"
        h "You would've been adorable with a scottish accent!"
        v "More like impossible to understand!"
        e "{size=-10} Shit that hurts {/size}"
        scene d6m20
        with dissolve
        l "Oi, ye hear'd the lass, no one would've understood her."
        c "Holy shit, that one got me good, that accent is amazing!"
        v "I didn't know your accent was that good Lou!"
        scene d6m21
        v "But, Elise, obviously this class won't help us, if anything, it exist to study us, keep us in a cage..."
        e "I know, but I've got a plan, a few days ago I remembered something."
        e "The dwarven kingdoms, especially the one of the north."
        h "The Dwarves? But they hate us!"
        e "... I know."
        scene d6m22
        c "Hmm... I'm up for it."
        c "I know a few dwarves, they're a nice bunch of hairy people!"
        e "With Goblins perhaps, but elves..."
        scene d6m23
        l "You all need to understand something, we are alone, we are the only one against the current society."
        l "Because we know the truth, if the dwarves are that 'kind' and welcoming, they'll accept us."
        scene d6m24
        with dissolve
        e "Hmm... Dwarves have great mages but they also made in forbidden magics, and exotic spells."
        e "The question is, when are we heading there?"
        scene d6m25
        c "Not now, I can't leave my sisters like that!"
        h "Nor my brother."
        v "Hmm..."
        scene d6m26
        v "It's a huge bet."
        l "The closest dwarven settlement is in the north, Feldberg in Germany."
        h "Can we teleport there?"
        e "Hmm perhaps yeah, although I would need days to prepare the trip, I can't take 4 people that easily."
        c "Well, Dwarves hide in small magic shaft anyway, so reaching them won't be that easy!"
        c "More intel would help."
        v "Now that I think about it, you never told us where do you come from Chumee."
        scene d6m27
        c "Oh really?"
        scene d6m28
        with fade
        c "Well I come from Eil'uxhol, means 'White mountain', it's near China actually, in the north of the country in the mountains."
        l "Oh, now that's interesting, and how did you met Elise?"
        c "You know, we often travel for commercial needs, export, import etc..."
        c "I met Elise in France a few years ago."
        scene d6m29
        e "The sassiest Goblin delivering the best goods!"
        e "I remember perfectly!"
        c "That was back when you decided to travel around Europe, how funny it was to see you in every major city!"
        v "Oh, that's so cute, a long lasting friendship."
        scene d6m30
        with fade
        c "And you butterfly, how did you met [name]?"
        scene d6m31
        v "Oh that's a long story..."
        v "I was only 4 when I met [name]."
        v "I lived deep in the Scottish countryside, with my mother..."
        v "[name] as always been..."
        menu :
            "This choice allows you to catch some relationship points, they all give the same amount of points shared along the girls."
            "Kind":
                scene d6m32
                $ELove += 2
                $CLove += 1
                $VLove += 2
                $HLove += 1
                $LLove += 1
                v "Kind, with everyone, he was incredibly open to talk."
                v "To help."
                v "Anyone, sometimes people abused it, sometimes people remember it and rewarded him."
                "Elise loves you more, Chumee loves you a bit more, Vanessa loves you more, Himia loves you a bit more, Lou loves you a bit more."
            "Impulsive":
                scene d6m33
                $CLove += 3
                $LLove += 2
                $VLove += 2
                v "Impulsive, he always listened to his instinct."
                v "Often it prooved him right, sometimes it didn't, but he got really confident in his own abilities."
                "Chumee loves you a lot more! Lou loves you more, Vanessa loves you more."
            "Brave":
                scene d6m34
                $ELove += 2
                $HLove += 2
                $VLove += 1
                $CLove += 1
                $LLove += 1
                v "Brave, he always stood up for me, always tried to do his best against the odds..."
                v "Sometimes... he failed, but he always rose back up."
                "Elise loves you more, Himia loves you more, Vanessa loves you a bit more, Chumee loves you a bit more, Lou loves you a bit more."


        scene d6m35
        h "You definitely seem to admire him."
        if CLove >= 9:
            c "Seems like I will have to share him with you~"
            v "W-What I-I"
            c "Calm down, I'm joking!"
            c "{size=-10} For now... {/size}"

        elif ELove >= 17:
            e "Sounds like we'll have share him Vanessa!"
            v "W-What I-I"
            e "Calm down, I'm joking!"
        else:
            l "Sounds like he will soon have a lot of people fighting for him!"
        scene d6m36
        h "Well Polygamy is allowed so it's totally possible..."
        v "What?"
        h "Well, even though it's not morally that great, what's wrong about loving someone, wether you're alone or 10..."
        v "I've never thought about it that way..."
        h "Of course people see this a bit weirdly, but who cares as long as you're around loved ones..."
        l "Awkward..."
        scene black
        "{b}Knock knock knock{/b}"
        with hpunch
        scene d6m37
        with dissolve
        doc "Elise, the Principal wants to see you in her office..."
        e "Hmm, really? What does she want?"
        doc "I don't know, but she seemed a bit annoyed, so be careful."
        scene d6m38
        with dissolve
        doc "Oh hi Vanessa!"
        v "H-hey Delphine..."
        doc "You're so cute, I hope you're doing alright, is your back ok?"
        v "It is thanks to you!"
        doc "Glad to hear it..."
        scene black
        "Meanwhile..."
        scene d6mcs
        o "Three days in a row!"
        o "You must really like us."
        m "Well, you both are good company, beside I don't have anything else to do."
        mi "Why did they get rid of you anyway?"
        scene d6mcs2
        m "Because they're afraid of humans, that's why."
        o "Of course they are, damn knife ears."
        m "Why do you hate elves so much?"
        o "Because they're assholes."
        scene d6mcs3
        m "I don't buy it, there is something else."
        o "*sigh*"
        stop music fadeout 1.0
        scene d6mcs4
        o "They experimented on me, kept me in a lab for years."
        scene black
        o "It all began 14 years ago..."
        play music "Opheliadream.mp3"
        o "I was barely 8, I lived with my parents in a small city near Geneva."
        o "After the war, the elves took my parents, and they took me too."
        o "The locked me in a room, and I could hear their voice through speakers."
        scene d6mcs5
        with fade
        o "Where are my parents? Where is my cat?!"
        scene d6mcs6
        with dissolve
        "Elf scientist" "Don't worry, your parents are doing good..."
        "Elf scientist" "You'll see your pet soon, don't worry we just want to make sure it's not sick."
        scene d6mcs5
        with dissolve
        o "She's a 'She'... her name is Mine!"
        scene d6mcs6
        with dissolve
        "Elf scientist 2" "Are you sure this is ethical? She's just a child?"
        "Elf scientist" "She's an insect at best, and a useful one."
        "Elf scientist" "Listen, if you want to help your parents, we will have to run tests on you..."
        scene d6mcs7
        o "T-tests?"
        "Elf scientist" "Don't worry it won't be painful."
        o "O-Ok..."
        scene d6mcs8
        with dissolve
        o "The room was old."
        scene d6mcs9
        with dissolve
        o "Filthy... I was an animal."
        o "And I hated it."

        "Elf scientist 2" "What? You want to overflow the room with Mana?!"
        "Elf scientist 2" "That would kill her!"
        "Elf scientist" "Test n°1 : Testing resistance of subject to excess of mana flows."
        scene d6mcs10
        with dissolve
        o "Wai-"
        play sound "Shock.mp3"
        scene black
        with flashbulb
        with hpunch
        o "{b}AAAAAAAAAAH{/b}"

        "Elf scientist 2" "You're absolutely mad!"
        "Elf scientist 2" "I'm freeing that poor kid..."
        "Elf scientist" "You're not doing anything, the cult has it's eyes on us, this child could destroy our efforts in the war."
        "Elf scientist" "She could fill humans with hope, hope that they too can use magic. We need those tests to ensure our domination."
        "Elf scientist 2" "But..."
        "Elf scientist" "No buts."
        scene d6mcs11
        with fade
        o "Y-y-y..-YOU SAID it wouldn't be painful!"
        scene d6mcs12
        with dissolve
        "Elf scientist" "Look, safe and sound."
        "Elf scientist" "Be strong, you'll get used to it..."
        scene black
        "Elf scientist" "Test n°2 : Test subject's resistance to Elements."
        o "NO WAIT-"
        play sound "Shock.mp3"
        scene black
        with flashbulb
        with hpunch
        o "{b}AAAAAAAAAAH{/b}"
        o "I've been here for so long."
        "Elf scientist" "Test n°9"
        scene black
        with flashbulb
        o "I stopped counting the hours."
        "Elf scientist" "Test n°23"
        scene black
        with flashbulb
        o "I just wanted my parents."
        "Elf scientist" "Test n°41"
        scene black
        with flashbulb
        o "They used shards, charged with mana and used spells against me, testing my resistance."
        o "Their theory?"
        o "I don't have any mana potential, but have the strongest genes of our species."
        o "How wrong they were."
        o "Each test was as twisted as the previous one, I was a beast, a lab rat."
        o "But I believed, I wanted my parents above anything else."
        m "This can't be the end?"
        o "Of course it's not..."
        o "But that's all I'm willing to share... For now."
        m "Shit."
        m "So Mine was still a cat back then?"
        mi "Yes, I was actually the only living thing allowed in her room."
        m "So, wait how did you turn human?"
        mi "You'll know it at the end."





































































































































































































































































jump Endingupdate



























































label Endingupdate:


    scene black

    s "This is the end of the Version 0.4 of Tales of Unity"
    s "More content is on it's way !"
    s "Tales of Unity is my 1st project, I put all of my heart, my love and my hopes into it."

    "Patreon Poll's results!"
    "The girl voted to get custom arts for v0.4 is Chumee!"
    "All arts can also be found in the custom art channels of the discord."
    scene cart1
    ""

    scene cart2
    with fade
    ""

    scene cart3
    with fade
    ""



    "The patreon voted!"
    "And the girl chosen by them to recieve an animated scene is Himia!"
    "It's obviously not canon."

    scene vid I
    ""
    scene black
    "For the next update, Chumee won't be in the Static custom art Poll, and Himia won't be in the Animated poll to preserve the variety of each arts!"







    "Special Thanks"

    s "Thanks to Runey for inspiring me to do this project while also helping me coding on Ren'py, check his game Harem Hotel if you haven't already!"
    s "Huge thanks to Lunalee, with his help I was allowed to make an Android version of the game!"
    s "Thanks Killer7 for trying my update, that lad is such a nice guy."
    s "Special Thanks to everyone that has been following me with this project, Aolli, Jam3s, Karne (Chumee, Daimee & Mahamee's designer), Meidyan, Parcel, Randymagnum, rndg, Dante!"
    s "Amak33 and warsson for inspiring me and following my work"
    s "Thanks to each one of my patrons for supporting me and allowing me to live out of my passion."
    s "And of course, thanks to you, player for giving a shot at my work."
    stop music fadeout 1.0
    s "You are the reason I decided to start this adventure!"
    "Most of the songs used are by 'Medyän', 'Lobo Loco' and 'Damiano Baldoni'"
    "Every asset used for this game belongs to Illusion."
    "If you enjoyed this game consider supporting Stronkboi on Patreon!"




    return






label gal_elise_1:
    if _in_replay:
        $ name = persistent.gallery_name

    scene black with dissolve
    "..." with vpunch

    scene vid
    with fade
    m "Elise... I-I love you!"
    e "I love you too [name]"
    e "I wanted this to happen for so long!"
    e "Just you and me, connected..."
    e "Relax now, it's just the two of us."
    e "Let me take care of you..."
    "..."
    scene black
    scene EWup1
    image EWup1 = im.Scale ("EWup1.png", 1920, 1080)
    with hpunch

    e "Wh..What..."
    scene black
    scene EWup2
    image EWup2 = im.Scale ("EWup2.png", 1920, 1080)
    with fade
    e "What a ...mmm... Dream."
    e "... [name]..."

    scene black with dissolve
    $ renpy.end_replay()
    return



label gal_chumee_1:
    if _in_replay:
        $ name = persistent.gallery_name

    scene black with dissolve
    "..." with vpunch

    scene black
    c "Fuck... this heat is fucking unbearable..."
    scene vid A
    c "I can't breath for 5 minutes without.. ah fuck! Needing that."
    c "It's ... fucking annoying, and yet it feels so good..."
    c "... Fuck ... [name]... I want... you..."
    c "... I need something... or else I'm gonna go crazy..."
    c "Shit! I can feel it coming!"

    scene vid B
    c "Ffffuuuucck..."
    c "..."
    c "Fuck... that was..."
    c "Intense..."
    c "I need... [name]..."

    scene black with dissolve
    $ renpy.end_replay()
    return

define euklid = Character('Евклид', color="#508aa5")
define sigmuses = Character('Сигмусы', color="#1e5e0a")
define warrior = Character('Воин', color="#1e5e0a")
define autokrat = Character('Автократ', color="#bf3131")
define sanya = Character('Саша', color="#05728d")
define alla = Character('Алла', color="#6581dd")
define alla_s = Character('Алла',image = 'alla', color="#6581dd")
define semen = Character('Семен', color="#32438f")
define stud = Character('Большинство студентов', color="#32438f")
define semen_s = Character('Семен',image = 'semen', color="#32438f")
define npc = Character('Мужчина', color="#1e5e0a" )
define cat = Character('Кот', color="#ee8f22" )
define student1 = Character('Студент 1', image = 'oleg', color = "#1239bb" )
define student2 = Character('Студент 2', image = 'ray', color = "#f49494" )
define oleg = Character('Олег', image = 'oleg', color = "#1239bb" )
define rayan = Character('Райан', image = 'ray', color = "#f49494" )
define teacher = Character('Святогор Великанович', color = "#1e5e0a" )
define teacher_s = Character('Святогор Великанович',image = 'teacher', color = "#1e5e0a" )
define radik = Character('Радик', color = "#ad5454")
define sec = Character('Секретарь', color = "#ad54ad")
define _dismiss_pause = False
define truth = True
define bit = 1
define open_count = 0
define lastPosl = 1
define dissolve = Dissolve(0.5)
define fastdissolve = Dissolve(0.25)

init python:
    renpy.music.register_channel('test_three', 'sfx', False)
    numbll = 0
    numbl = 0
    numbc = 0
    numbr = 0

screen safe_code:
    modal True
    imagemap:  
        ground "images/safe_i/cl_panel.png"
        idle "images/safe_i/cl_panel.png"
        hover 'images/safe_i/cl_panel_.png'
        
        hotspot(1050, 447, 79, 45) action If(numbll == 1, If(numbl == 1, If(numbc == 2, If(numbr == 0, [Hide("safe_code"), Jump ('start13')], Jump ('access_denied')), Jump ('access_denied')), Jump ('access_denied')), Jump ('access_denied'))

    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .40 yalign .28 action [Play('test_three', 'safe.mp3'), If(numbll < 9, SetVariable("numbll", numbll + 1), SetVariable("numbll", 0))]
    add "images/safe_i/cl_%s.png"%(numbll) xalign .40 yalign .33 zoom 0.27
    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .40 yalign .43 action [Play('test_three', 'safe.mp3'), If(numbll > 0, SetVariable("numbll", numbll - 1), SetVariable("numbll", 9))]
    
    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .44 yalign .28 action [Play('test_three', 'safe.mp3'), If(numbl < 9, SetVariable("numbl", numbl + 1), SetVariable("numbl", 0))]
    add "images/safe_i/cl_%s.png"%(numbl) xalign .44 yalign .33 zoom 0.27
    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .44 yalign .43 action [Play('test_three', 'safe.mp3'), If(numbl > 0, SetVariable("numbl", numbl - 1), SetVariable("numbl", 9))]
    
    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .48 yalign .28 action [Play('test_three', 'safe.mp3'), If(numbc < 9, SetVariable("numbc", numbc + 1), SetVariable("numbc", 0))]
    add "images/safe_i/cl_%s.png"%(numbc) xalign .48 yalign .33 zoom 0.27
    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .48 yalign .43 action [Play('test_three', 'safe.mp3'), If(numbc > 0, SetVariable("numbc", numbc - 1), SetVariable("numbc", 9))]
    
    imagebutton auto "images/safe_i/up_%s.png" focus_mask True xalign .52 yalign .28 action [Play('test_three', 'safe.mp3'), If(numbr < 9, SetVariable("numbr", numbr + 1), SetVariable("numbr", 0))]
    add "images/safe_i/cl_%s.png"%(numbr) xalign .52 yalign .33 zoom 0.27
    imagebutton auto "images/safe_i/dwn_%s.png" focus_mask True xalign .52 yalign .43 action [Play('test_three', 'safe.mp3'), If(numbr > 0, SetVariable("numbr", numbr - 1), SetVariable("numbr", 9))]
    
label access_denied:
    $ open_count += 1

    if open_count >= 3: 
        hide screen safe_code
        jump start13

    euklid 'Ой попробую ещё раз'

    show screen safe_code

label start: 
    stop music fadeout 1
    window hide
    scene black_background
    pause 1
    scene disclaimer with Dissolve(2)
    $ renpy.pause(3, hard=False)
    scene black_background with Dissolve(3)
    window show

    play sound autokrat 

    autokrat '[euklid], не забывай своё предназначение. Империя рассчитывает на тебя.'

    sanya "Грубый мужской голос раз за разом раздавался в моей голове."

    sanya "Хотелось укрыться от него, сделать всё что угодно, лишь бы не слышать уже выученные наизусть строки."

    sanya 'Я открыл глаза...'

    play music bl
    scene hospital fade start with fade
    scene  hospital_fade with dissolve
    scene hospital_fade1 with dissolve
    scene hospital_fade2 with dissolve
    scene hospital_1st_scene with dissolve

    sanya 'Яркий, ослепляющий свет освещал всю комнату, вокруг меня стояли пустые койки, кажется совсем недавно на них ещё кто-то лежал. Из окна раздавалось еле слышимое щебетание птиц.'

    sanya 'Наконец-то тишина... Как же я долго этого ждал.'

    play sound door_open

    'Вдруг больничная дверь открывается и в палату входит симпатичная блондинка.'

    'Она медленно идет прямо к моей койке, смотря себе под ноги и напевая какую-то незамысловатую мелодию.'

    show alla 1_ with easeinright

    sanya 'Эм, здравствуй...Ты совсем не изменилась, Алла, опять витаешь в облаках.'

    show alla amazed with dissolve

    'Блондинка на секунду замирает на месте, направляет свой взор на меня и громко, что есть мочи начинает кричать.'

    show alla sad 0_1 with dissolve
    
    alla 'САША, ТЫ НАКОНЕЦ-ТО ОЧНУЛСЯ!'

    sanya 'Звонкий девичий крик на секунду оглушил меня. Да что там крик, это было больше похоже на вой противопожарной сирены. Моя подруга детства была самым громким человеком, которого я когда-либо знал.'

    sanya 'Тишина была недолгой...'

    'Девушка, всхлипывая продолжила говорить.'

    show alla sad_1 with dissolve

    alla 'Ты не представляешь, как я за тебя волновалась, как все волновались. Мы начали думать, что ты не очнёшься, а твой младший брат уже занял комнату, в которой ты жил. Как же хорошо, что ты очнулся!'
  
    sanya 'Пожалуйста, можешь успокоиться, у меня до сих пор болит голова.'

    show alla sad smile1_1 with dissolve

    alla 'Ах, конечно, прости меня. Что я могу для тебя сделать?'

    sanya 'Для начала позови врача.'

    alla 'Ой, точно, надо было это сделать с самого начала. Я сейчас вернусь, никуда не уходи.'

    hide alla sad smile1_1 with moveoutright

    play sound door_close

    'Девушка быстро побежала в обратном направлении, попутно хлопнув дверью.'

    sanya 'Пока эта шумная особа не вернулась, надо осмотреться.'

    sanya 'Я попытался встать, поначалу ноги меня совсем не слушали, но спустя время я наконец-то сделал свои первые шаги.'

    sanya 'Встав с койки, я подошёл к маленькому настенному зеркалу.'

    show mirror 2 with fade

    sanya 'На меня смотрел худой, бледный, короткостриженый мужчина с коричневыми волосами и {i}ярко зелеными глазами{/i}.'

    hide mirror with fade

    sanya 'Осмотрев палату, ничего полезного я не нашёл, кроме странных розовых тапочек.'

    show tapki1 with dissolve

    menu:
        
        'Как быть с тапочками?'

        'Надеть их':
            jump divarication_a

        'Пойти босиком':
            jump divarication_b

    label divarication_b:

        sanya 'Ну уж нет, лучше пойду босиком, чем в этом.'

        play sound door_open

        scene black_background with fade

        play sound door_close

        'Когда я вышел в коридор, передо мной открылся огромный холл больницы.'

        jump start2

    label divarication_a:

        'Недолго думая, я надел эти тапочки и вышел в коридор.'

        play sound door_open

        scene coridor with fade

        play sound door_close

        show men 1_ with dissolve

        'Вдруг, огромный, мимо проходящий, мужчина остановился около меня.'
        
        npc 'Эй, сопляк, тебя не учили, что брать чужое нельзя? А ну быстро снял мои любимые тапочки!'

        sanya 'Меня переполнила злоба. Как он смеет так со мной обращаться. Но понимая, что против такого бугая у меня мало шансов, я послушно выполнил его просьбу.'

        sanya 'Простите, пожалуйста, я просто перепутал. Вот ваши прекрасные тапочки.'

        scene black_background with fade

        sanya 'Получив от меня своё драгоценное сокровище, здоровяк пошёл дальше. А передо мной открылся огромный холл больницы.'

        jump start2
    
label start2:

    scene coridor with fade

    menu:

        'Куда пойти?'

        'Пойти направо':
            jump right

        'Пойти прямо':
            jump top

        'Пойти налево':
            jump left

    label left:

            sanya 'Я повернул налево, бродя между бесчисленного количества палат, я уперся в дверь с надписью «ВЫХОД»'

            stop music fadeout 3.0

            sanya 'Вдруг кто-то схватил меня за руку и силой заставил развернуться.'

            play music beautiful_rain

            'Это была Алла.'

            show alla smile with dissolve

            alla 'Поймала, хе-хе. От меня так просто не убежишь.'

            jump start3
    
    label right:

        scene black_background with fade

        sanya 'Бродя вдоль коридора, я в конце концов уперся в тупик, поэтому вернулся назад.'

        jump start2
    
    label top:

        sanya 'Я решил пойти прямо, пока не дошёл до двери.'

        show toilet door with dissolve

        menu:

            'Следующее действие?'

            'Войти':
                jump enter

            'Развернуться и пойти обратно':
                jump start2
        
        label enter:

            play sound door_open_

            show toilet door opened with dissolve

            scene toilet with fade

            sanya 'Открыв дверь, я сразу почувствовал смердящий запах, от которого у меня начали слезиться глаза.' 

            sanya 'Это был мужской туалет, пока меня не вырвало, я решил вернуться обратно.'

            jump start2

        
label start3:

    sanya 'Фух, Алла, это всего лишь ты...'

    show alla angry with dissolve

    alla 'Всего лишь я!? Опять хочешь попасть на больничную койку?'

    sanya 'Нет, конечно, ты просто меня очень напугала.'

    show alla angry very with dissolve

    alla 'Значит я страшная, да!? Видимо, тебе очень нравится в больнице.'

    sanya 'Умеешь ты делать из мухи слона.'

    alla 'Так я еще и истеричка...'

    sanya 'Чтобы хоть как-то спастись от гнева девушки, я взял её за руку.'

    show alla confused with dissolve 

    '...'

    sanya 'Алла, доктор меня, наверное, уже обыскался, я вернусь в палату.'

    show alla smile with dissolve

    alla 'Хорошо, на этот раз я тебя прощаю. Буду ждать на улице, поторапливайся.'

    sanya 'Оставив девушку, я пошел в сторону своей палаты.'    

    hide alla smile with dissolve 

    play sound door_open

    scene doc_ with fade

    sanya 'Зайдя в помещение, я увидел ждущего меня доктора. Он проверил мою температуру и измерил пульс.'

    sanya 'Не обнаружив никаких аномалий, доктор разрешил мне выписаться из больницы.'

    scene black_background with dissolve

    sanya 'Когда он вышел, я смог переодеться в ту одежду, которую успела мне принести Алла.'

    play sound door_close

    sanya 'Взяв с собой всё необходимое, я направился к выходу.'

    scene street with dissolve

    show alla 1_ with dissolve

    '...'

    show alla happy with dissolve

    alla 'Я уже думала, что простою здесь вечность.'

    sanya 'Не преувеличивай, меня не было от силы минут 15.'

    show alla smile 2 with dissolve

    alla 'Ладно-ладно, пойдем скорее в институт, мы ещё успеваем на последнюю пару.'

    sanya 'Какой ещё институт!? Меня только что выписали из больницы, я должен отдыхать!'

    show alla smile 3 with dissolve

    alla 'Ты в прошлом году так отдохнул, что сейчас находишься на грани отчисления. В деканате сказали, что если ты сегодня не явишься на пары, то можешь больше в институт не приходить.'

    sanya 'А откуда они узнали, что я очнулся?'

    show alla smile hand with dissolve

    alla 'Хе-хе...'

    sanya 'Спасибо, подруга... Тогда пошли, что уж там.'

    scene irit_cat with dissolve

    show alla smile 2 with dissolve

    sanya 'Фух, как же я люблю это место.'

    alla 'Именно поэтому появляешься тут раз в полгода?'

    sanya 'Любить из дома намного приятнее.'

    sanya 'Неожиданно я почувствовал, как кто-то хлопает меня по плечу. Обернувшись, я увидел своего старого друга – Семёна.'

    hide alla smile 2 with fastdissolve
    show semen with dissolve

    semen 'Ё-маё, кого я вижу. Саня, неужели это ты? Как ты поживаешь?'

    sanya 'Привет, Семён. Всё супер, чувствую себя прекрасно. Только вот...'

    'Перебив меня, Семён продолжил.'

    show semen laugh with dissolve

    semen 'Это как надо было умудриться, придя впервые за полгода в институт, отравиться на перемене шаурмой и два часа не выходить из туалета, ё-маё.'

    semen 'А потом еще в больнице пролежать без сознания месяц. Когда об этом узнали ребята с потока, ржали весь день.' 

    show semen smile with dissolve

    semen 'Теперь ты у нас местная легенда, говорят, что после тебя еще неделю никто не заходил в этот туалет, ё-маё.'

    sanya 'А откуда об этом все узнали?'

    hide semen smile with fastdissolve
    show alla smile hand with dissolve

    alla 'Упс, хе-хе.'

    sanya 'Вариант с отчислением теперь не кажется мне настолько плохим...'

    'Пока мы болтали, незаметно пролетело время, вот-вот должна была начаться последняя пара.'

    show alla smile with dissolve

    alla 'Ну что, пора заходить.'

    scene irit_cat with dissolve

    'Уже почти подойдя ко входу, краем глаза я заметил некий пушистый комок, сидящий на ближайшем ко входу дереве.' 

    hide alla smile with fastdissolve
    show cat_ with dissolve

    'Приглядевшись, я разглядел рыжего кота, который вот-вот собирался прыгнуть.'

    #картинка с котом

    play sound meow

    cat 'Мяууууу'

    menu:

        'Следующее действие?'

        'Помочь коту спуститься':
            jump help

        'Продолжить смотреть':
            jump watch
    
    label help:
        
        show cat_and_sanya with dissolve
        hide cat_

        'Я подошёл к дереву. Ветка, на которой сидел котик была на пару сантиметров выше моего роста, так что я свободно мог дотянуться до рыжего создания.'

        sanya 'Иди сюда, рыжик.'

        show cat_and_sanya1 with dissolve
        hide cat_and_sanya

        play sound cat_noize

        'Кот, смотря на меня, так громко зашипел и встал на дыбы. Я попробовал подойти чуть ближе.'

        scene irit with dissolve

        'В этот момент кот, продолжая шипеть, сам спрыгнул с ветки, приземлился на четыре лапы и побежал прочь.'

        jump start4
    
    label watch:

        'Решив, что ничем помочь я не смогу, я просто продолжил смотреть, что произойдет дальше.'

        show cat_and_alla with dissolve

        hide cat_ 

        'Однако, моя подруга думала по-другому, поэтому сразу же понеслась к бедному животному и аккуратно помогла ему спуститься.'     

        scene irit_cat1 with dissolve

        play sound murk

        'Рыжий кот, опустившись на землю, обвился у ног своей спасительницы и начал мурлыкать.'

        play sound cat_noize

        'Мы с Семёном решили подойти, но как только кот увидел меня, он зашипел и попятился назад.'

        scene irit with dissolve

        jump start4

label start4:

    sanya 'Странно, обычно животные спокойно ко мне относятся, а этот...Видимо бешеный.'

    show semen sus with dissolve

    semen 'Стопудово, он увидел в тебе соперника. Вот у вас даже глаза {i}одинакового цвета{/i}.'

    sanya 'Что?'

    hide semen sus with fastdissolve

    show alla smile 3 with dissolve

    alla 'А, точно, тоже хотела спросить, как давно ты носишь зеленые линзы, ведь раньше у тебя были {i}серые глаза{/i}.'

    'Точно, ещё в больнице, смотря в зеркало, я заметил что-то странное. Почему мои глаза стали {i}зелёными{/i}?'

    stop music fadeout 3
    play sound fall 
    scene black_background with Dissolve(3) 

    play sound autokrat

    autokrat 'Евклид, не забывай своё предназначение. Империя рассчитывает на тебя.'

    play music dark

    sanya 'Опять этот странный мужской голос пронзил мои уши. Ещё чуть-чуть и голова бы взорвалась.'

    scene space a with fade

    euklid 'В АТАКУ!'
    
    play sound sword

    warrior 'Слушаемся, генерал!'
    
    'Спустя несколько минут оглушающий лязг мечей и стоны врагов прекратились.'

    stop sound fadeout 2.0

    play music dark

    scene space b with fade

    euklid 'ПЛАНЕТА ЕТ-5681 ЗАХВАЧЕНА!'

    play sound yaa

    warrior 'Ура! Славься великая раса Сигмусов!'

    'Со всех сторон послышались восхищенные вопли моих подчинённых. Понимая, что моя миссия выполнена, я наконец-то вздохнул с облегчением.'

    warrior 'Генерал, мне только что передали, что великий император желает вас видеть.'

    euklid 'Хорошо, тогда оставшиеся дела я поручаю тебе.'

    scene black_background with fade

    stop music fadeout 3

    'Покинув захваченную территорию, я телепортировался в замок Великого императора.'

    scene autokrat_scene with dissolve

    play music dark

    euklid 'Да здравствует его величество Великий император Автократ!'

    autokrat 'Здравствуй, Евклид. Я очень доволен тобой, с момента нападения на ЕТ-5681 прошло всего три месяца, а планета уже захвачена.'

    euklid 'Великий Император, это полностью заслуга нашей армии.'

    autokrat 'Евклид, ты же знаешь, что мне уже 566 лет. Увы, вечно править я не могу, поэтому я ищу человека, которому могу передать трон.'

    'Грозный мужчина на секунду остановился, оценочно оглядел меня с ног до головы и продолжил свою речь.'

    autokrat 'И ты больше всего подходишь на эту роль.'

    euklid 'Великий император, да как я смею даже думать об этом.'

    autokrat 'НЕ СПОРЬ СО МНОЙ! Раз я сказал, то так и будет.'

    euklid 'Слушаюсь, повелитель.'

    autokrat 'Ты же в курсе о моей давней мечте? Планета Терра, иначе называемая Землей.'

    autokrat 'Когда я был еще совсем юным, примерно твоего возраста, мы с моими братьями пытались её захватить, но, как видишь, безуспешно.'

    autokrat 'Ты знаешь откуда у меня эти шрамы?'

    euklid 'Его величество получил их в войне?'

    autokrat 'Нет, этот шрам мне оставило чудовище, которое обитает на этой планете. Местные жители держат их в качестве домашних животных и называют {i}котиками{/i}...Что за суровые люди там живут.'

    autokrat 'Итак, Евклид, если ты взломаешь волшебный камень, который контролирует этих чудовищ, то станешь следующим императором Сигмусов. Согласен ли ты?'

    menu:

        'Согласиться взломать волшебный камень?'

        'Отказаться':
            jump refuse

        'Принять предложение':
            jump accept
        
    label refuse:

        euklid 'Великий император, мне очень лестны ваши слова, но я, пожалуй, откажусь. Думаю, что не справлюсь с данной задачей.'

        euklid 'К тому же на Венере открыли новую базу отдыха, я как раз хотел взять отпуск после захвата...'

        autokrat 'Я же говорил не спорить со мной.'

        autokrat 'Или ты отправляешься на миссию, или будешь гнить до конца своей жизни в межгалактической тюрьме.'

        '*Оказаться в межгалактической тюрьме, в которой отбывали свои сроки бывшие короли планет, завоеванных Сигмусами, было сравни смертному приговору.*'

        stop music fadeout 2

        euklid 'Хорошо, я согласен.'

        jump start5

    label accept:

        euklid 'Буду рад служить, Великий император.'

        autokrat 'Я в тебе не сомневался, Евклид. По нашим данным, волшебный камень находится в месте, которое люди называют «институт».'

        autokrat 'Я вселю тебя в тело местного жителя, и ты должен найти и взломать камень.'

        euklid 'Слушаюсь, Великий император.'

        stop music fadeout 2

        autokrat 'Евклид, не забывай своё предназначение. Империя рассчитывает на тебя.'

        jump start5

label start5:

    scene black_background with fade

    play sound tin

    alla 'Саша, ты в порядке? Быстрее вызывайте скорую!'

    'Я открыл глаза, передо мной предстало заплаканное лицо блондинки.'    

    scene irit with dissolve 

    show alla sad_1 with dissolve

    'Я быстро сориентировался где я нахожусь, повезло, что воспоминания бывшего владельца тела не исчезли вместе с его душой.'

    play music para 

    euklid 'Я в норме, не надо никакой скорой.'

    alla 'Саша, боже мой, ты так меня напугал, когда резко упал в обморок.' 

    alla 'Ты был прав, не стоило тебе идти сегодня на пары, прости меня.'

    hide alla sad_1 with fastdissolve

    show semen n with dissolve

    semen 'Ё-маё, ты так эпично шлёпнулся о землю, жаль не получилось заснять это на память.'

    hide semen n with fastdissolve

    show alla angry with dissolve

    alla 'Семён, думай о чём говоришь, иначе шлёпнешься уже ты.'

    euklid 'Да ничего страшного, не злись на него. И вправду глупо получилось, я просто не удержал равновесие и упал на ровном месте, видимо головушкой стукнулся и отключился.'

    show alla amazed with dissolve

    euklid 'Пойдёмте быстрее на пару.'

    alla 'Тебе надо сначала сходить к врачу, вдруг сотрясение.'

    euklid 'Я же говорю, что чувствую себя хорошо, идём быстрее.'

    stop music fadeout 1.0

    scene ir with fade

    play music balagan

    euklid 'Вау, здешние технологии выглядят довольно продвинутыми!'

    euklid 'А еще тут довольно шумно!'

    scene aud with fade

    'Зайдя внутрь аудитории, я решил занять место поближе к первому ряду. Дойдя до второго ряда, я устроился поудобнее. Семён и Алла сели рядом со мной.'

    alla_s amazed 'Почему ты вдруг решил сесть так близко, раньше ты обычно занимал последние ряды.'

    semen_s amazed 'Ага, говорил, что это идеальное место, чтобы отоспаться.'

    euklid 'Хочу взяться за ум и стать хорошим специалистом.'

    hide semen_s with dissolve

    'Ребята резко начали громко смеяться.'

    semen_s laugh 'Скажешь тоже, стать хорошим специалистом, ах-ха-ха.'

    alla_s smile2 'Ага, быстрее Семён съедет от мамы, чем ты получишь оценку выше 2, хе-хе.'

    semen_s angry 'Эй, про маму было лишнее.'

    alla_s smile 'Прости-прости…'

    'Вдруг чья-то рука похлопала Аллу по плечу.'

    student1 sad 'Молодые люди, я вообще-то учиться сюда пришёл, а не слушать вашу болтовню.'

    semen_s smile 'Ну так и не слушай, в чём проблема?'

    'Внезапно в диалог вмешался парень, сидящий рядом с недовольным студентом.'

    student2 horny 'Он прав, Олежик. Тем более преподавателя пока нет, расслабься. Хочешь я сделаю тебе массаж?'

    oleg amazed 'Райан, ты на чьей стороне?' 

    oleg careless 'И вообще, отстань от меня, мы находимся в новелле с возрастным ограничением 12+, если продолжишь в том же духе, у авторов могут возникнуть проблемы.'

    rayan glad 'Хо-хо-хо, молчу-молчу, любишь ты говорить какие-то странные вещи.'

    'Я удивлённо посмотрел на Аллу и Семёна.'

    semen_s laugh 'А что ты хотел? На радиофаке дефицит девочек, ребята выкручиваются как могут.'

    oleg angry 'Эй, вы сейчас про нас болтаете?'

    'Чувствуя, что обстановка накаляется до предела, я обернулся лицом к недовольному парню и посмотрел прямо в глаза.'

    euklid 'Забудь всё то, что сейчас было и займись своими делами.'

    'Он на секунду закрыл глаза, а потом как ни в чем не бывало стал что-то писать в своей тетради.'

    'Хорошо, что хоть какие-то способности у меня остались'

    'Повернувшись обратно, я заметил на себе взгляд Семёна.'

    'Он оглядел меня с ног до головы, остановил свой взгляд на глазах и что-то пробормотал себе под нос.'

    semen_s podoz 'Подозрительно…'

    stop music fadeout 2.0

    play music para fadein 5.0

    show teach sad with Dissolve(1)

    'В этот момент в аудиторию вошёл высокий, подкаченный мужчина. На вид ему было лет 50.'

    show teach smile 2 with dissolve

    npc 'Привет, молодёжь, или как мы с вами любим говорить по-модному привет-медвед, молодёжь.'
 
    show teach with fastdissolve

    'В аудитории воцарилась давящая тишина, казалось, что можно услышать взмах крыльев бабочки, порхающей за окном.'

    semen_s smile 'Дед опять за старое…'

    show teach smile 2 with fastdissolve

    npc 'Ох, ну ладно. Для тех, кто не в курсе, звать меня Святогор Великанович, я ваш преподаватель по информационной безопасности.'

    teacher 'Вот мой номер +797777777.... и моя почта nenavizhu.yashcherov@mail.ru, если вам будет грустно и одиноко, вам будет не с кем поговорить, свяжитесь со мной.'

    teacher 'А, ну и по вопросам учебы тоже.'

    show teach smile with fastdissolve

    teacher 'А теперь начнём и саму пару, а именно с теории. Начнём с простого, кто скажет мне определение Информационной безопасности?'

    'Семён резко потянул руку вверх, надеясь ответить раньше, чем кто-либо.'

    semen_s smile 'Информационная безопасность - это охрана информации от различных угроз по типу кражи или уничтожения.'

    show teach smile 2 with fastdissolve

    teacher 'Ого, думающая голова, правильно говорите.'

    teacher 'Так, а может кто-нибудь назвать мне основную задачу информационной безопасности?'

    show teach with fastdissolve

    'Семён вновь потянул руку.'

    show teach sad with dissolve

    teacher 'Так, ну что же, Cемён, извольте же вновь ответить на мой вопрос!'

    show teach with fastdissolve

    semen_s smile 'Основная задача информационной безопасности - защитить данные, сохраняя производительность компании.'

    show teach smile 2 with dissolve

    teacher 'А этот парень точно метит на 100 баллов! Cпасибо, Семён, за ваш ответ, можете больше не отвечать, а то всё-таки я преподаватель, а не вы.'

    'Святогор Великанович с улыбкой усмехнулся и продолжил дальнейшую тему сам.'

    show teach smile 2 with dissolve

    teacher 'В основе нашей специальности лежит деятельность по защите информации — обеспечению её конфиденциальности и целостности, а также недопущению какой-либо компрометации в критической ситуации.'

    teacher 'К таким ситуациям относятся природные, техногенные и социальные катастрофы, компьютерные сбои, физическое похищение и тому подобные явления.'

    teacher 'С ростом числа цифровых технологий на предприятиях, специалисты по защите секретных данных становятся более востребованными.'

    show teach with dissolve

    teacher 'Крупнейшие предприятия и организации, в силу жизненной важности и ценности информации для их бизнеса, нанимают их, как правило, себе в штат и зачастую платят неплохие деньги.'

    teacher 'В задачу специалистов по ИБ входит противостояние кибератакам, зачастую нацеленным на похищение важной конфиденциальной информации или на перехват управления внутренними системами организации.'

    show teach sad with dissolve

    'Евклид в мыслях был глубоко удивлён, что существует такая вещь как информационная безопасность, а также настолько она полезна.'

    'Пока преподаватель говорил, он записывал основные моменты, а студенты, которые изначально были бодрыми и заряженными, уже готовы были взмолиться всем богам, лишь бы не быть на этой паре.'

    rayan dis 'Омайгадбл, только 1 пара, а уже столько информации, почему так сложно...'

    oleg amazed 'Райан, я тебя понимаю, как можно вообще столько говорить и не теряться в мыслях, что за мужик... Вот бы сейчас в школу, там-то явно проще было, а лучше сразу домой...'

    rayan sad 'Олежик, ты абсолютно прав, лучше бы я не поступал  в этот ВУЗ.'

    'Евклиду надоело нытье этих нерадивых студентов, поэтому он решил тихо сказать им, что думает об их отношении к учёбе.'

    euklid 'Боже, да что вы за люди такие, пара только началась а вы уже разнылись.' 
    
    euklid 'Попытайтесь внимательно послушать преподавателя, вслушаться в его слова и того вы определённо что-то поймёте.'

    euklid 'Надеюсь не для того же вы поступали сюда чтобы ныть о том как вам "тяжело".'

    'Студенты были в шоке от прямоты, они умолкли и обратили свой взгляд на оратора в попытках понять его речь.'

    rayan dis 'Иу, какой-же ты зануда.'

    euklid 'Ну и ну, нужно же быть такими… У нас образование могут получать только {i}члены королевской семьи{/i}, а тут у людей столько возможностей, а они…'

    rayan dis 'Что за королевская семья? Ты в своём уме?'

    'Чёрт, взболтнул лишнего, хорошо, что только один человек обратил на это внимание, надо бы его загипнотизировать.'

    show teach smile 2 with fastdissolve

    teacher 'Так, ну на сегодня, пожалуй, остановимся, дам вам немного передохнуть!'

    hide teach smile 2 with dissolve

    'Студенты, что сидели рядом с Евклидом, свалились без сил ровно с теми же мыслями, что и час назад.'

    'Казалось, что они готовы были уже потерять сознание, ведь до сих пор в их головы не поступало столько информации.'

    'Евклид же был бодрячком и перечитывал то, что не так давно слушал, дабы передать всю самую важную информацию в лучшем виде для своих союзников.'

    semen_s smile 'Слушайте, может после этой пары пойдём прогуляемся, всё равно же больше пар на сегодня у нас нет?'

    alla_s smile 'Хм, а что, звучит хорошо, после такого точно нужно подышать свежим воздухом... Саша, ты как?'

    'Сегодня я и так вёл себя подозрительно, как раз то, что мне нужно, потрусь с этими людишками, а потом приступлю к своим делам.'

    euklid 'Да, конечно, почему бы и нет.'

    semen_s smile 'Крутяк! Тогда будем ждать тебя на выходе у института!'

    'Спустя несколько минут вернулся преподаватель.'

    show teach sad with dissolve

    show teach smile 2 with fastdissolve

    teacher 'Так-с, ну что же, студенты, вы устали, да?'

    stud 'ДАА!'

    show teach smile with fastdissolve

    teacher 'Хо-хо, понимаю, тогда не буду вас долго мучить и сразу же перейду к домашнему заданию, а там уж и отпущу вас!'

    show teach smile 2 with fastdissolve

    teacher 'Внемлите же словам моим! Задание вот какое: Повторите весь пройденный материал на этой лекции, в следующий раз он вам пригодится!'

    teacher 'Все желающие уйти свободны, а те, кто хочет получить сюрприз, прошу остаться на своих местах!'

    scene aud empty teacher with dissolve

    'Я, Семён, Алла и несколько других студентов решили остаться в ожидании сюрприза.'

    alla_s smile 'Как думаете, что за сюрприз? Может автомат по предмету?'
    scene aud empty 
    show teach sad
    semen_s smile 'Да вряд ли, думаю просто пару баллов в ведомость.'

    show teach smile 2 with fastdissolve

    teacher 'Так-с, господа смельчаки, вот вам мой сюрприз!'

    show teach sad with fastdissolve

    teacher 'Прошу вас подойти и взять по листку.'
    
    scene aud empty list with dissolve
    show teach sad with fastdissolve

    'Все подошли и, взяв по листку, разошлись.'

    semen_s podoz 'Блин, дед опять всех одурачил.'

    scene aud empty list_
    show teach sad

    alla_s angry 'В какой раз мы на это попадаемся, сегодня надо было уходить со всеми.'

    show teach smile 2

    teacher 'Как вы могли уже заметить, это небольшой тест по терминам, которые мы сегодня проходили.'

    teacher 'Времени у вас не так уж и много, потому и вопросов мало.' 

    teacher 'Как только закончите решать, подойдите ко мне и отдайте тест с вашими ответами.'

    show teach sad with fastdissolve

    euklid 'Так, ну вроде ничего особо сложного тут и нет, вот 1 вопрос:'

label start6:

    menu:

        '«Основными источниками угроз информационной безопасности являются все указанные в списке: »'

        '1. Хищение жестких дисков, подключение к сети, инсайдерство.':
            jump firstfirst

        '2. Перехват данных, хищение данных, изменение архитектуры системы.':
            jump secondfirst

label firstfirst:

    euklid 'Ой, как же я так сглупил! Ладно, нужно двигаться дальше и не допустить ошибок там!'
    jump question2

label secondfirst: 

    euklid 'Хм, думаю второй вариант, так, что же там дальше... «Виды информационной безопасности:»'
    jump question2

label question2:

    menu:

        '«Виды информационной безопасности: »'

        '1. Персональная, корпоративная, государственная':
            jump firstsecond

        '2.Клиентская, серверная, сетевая':
            jump secondsecond

label firstsecond:

    euklid 'Так, думается мне, что правильный ответ под номером 1, интересно какой последний вопрос... '
    jump question3

label secondsecond:

    euklid 'Ух, надеюсь в этот раз я не прогадал и всё правильно, интересно какой последний вопрос...'
    jump question3

label question3:

    menu:

        '«Цели информационной безопасности – своевременное обнаружение, предупреждение: »'

        '1. Инсайдерства в организации':
            jump timeOut

        '2. Чрезвычайных ситуаций':
            jump timeOut

        '3. Не выбирать ничего':
            jump nothing

label timeOut:
    
    euklid 'Так, ну вроде это правильно.' 

    euklid 'Ладно, уже времени нет думать по второму кругу, нужно идти сдавать работу'

    jump start7

label nothing:

    euklid 'Странно, но именно в этом вопросе появился третий вариант ответа, да и по логике первые два не подходят, значит это точно он!'

    'Я, сделав выбор, молча встал со своего места, сдал работу и вышел из аудитории.'

    stop music fadeout 2.0

    jump start7

label start7:
    scene black_background with fade

    'На выходе из института меня уже ждали Семён и Алла.'

    scene irit with fade

    show alla 1_ with dissolve

    alla 'Что ты там так долго делал?'

    euklid 'То же самое, что и все — писал тест.'

    show alla amazed with dissolve

    alla 'Я тебя совсем не узнаю, раньше не ходил месяцами на пары, а тут вдруг…'

    euklid 'Решился взяться за ум, ты же сама говорила, что я на грани отчисления.'

    hide alla with fastdissolve
    show semen sus with dissolve

    semen 'Странно всё это…'

    play music beautiful_rain 

    show semen smile with dissolve

    semen 'Впрочем, хватит болтать, пойдёмте скорее есть, ё-маё.'

    scene black_background with fade

    'Мы послушно согласились с предложением нашего товарища.'

    'Через 5 минут мы дошли до захудалой забегаловки.'

    scene shawarma_1 with fade
    show alla amazed with dissolve

    alla 'Семён, куда ты нас привёл?'

    hide alla amazed with fastdissolve
    show semen smile with dissolve

    semen 'Как куда? В лучший ресторан Екатеринбурга!'

    hide semen smile with fastdissolve
    show alla smile 3 with dissolve

    alla 'Разворачиваемся, Саша, поедим в другом месте.'

    hide alla smile 3 with fastdissolve
    show semen amazed with dissolve

    semen 'Эй, сначала попробуйте что-нибудь, потом делайте выводы.' 

    show semen n with dissolve
    
    semen 'Официанта нам, пожалуйста.'

    'Тут из-за угла показался мужчина, он быстро подошёл к нам и заговорил.'

    hide semen n with fastdissolve
    show radik smile a with dissolve

    npc 'Вай, дружище, сколько лет, сколько зим.'

    semen_s amazed 'Но я же только вчера заходил…'

    'Не обратив внимание на слова Семёна, мужчина продолжил.'

    show radik smile c with dissolve 

    npc 'О, да ты не один!'

    show radik smile t with dissolve
    npc 'Добро пожаловать в лущщий ресторан - «Шаурма у Радика». Я, кстати, {i}Радик Слах Рахмуни Султан Иванов{/i}, но для вас просто Радик.'

    semen_s smile 'Нам, пожалуйста, три фирменных шаурмы.'

    alla_s angry 'Я не буду, Саша тоже.'

    show radik amazed with dissolve

    radik 'Вай-вай, девущк, вы отказываетесь от лучший блюда в своей жизни.'

    show radik smile c with dissolve

    radik 'Если вы переживаете по поводу тараканов, так я их вчера потравил, мамой клянусь. Почти всех…'

    semen_s amazed 'Почему ты решаешь за Саню?'

    alla_s angry 'Так он совсем недавно {i}отравился{/i}, между прочим тоже {i}шаурмой{i}.'

    semen_s smile 'Я тут каждый день ем и жив ещё. Саня, будешь шаурму?'

    menu: 

        'Как поступить?'

        'Заказать шаурму':
            jump order

        'Отказаться':
            jump order_refuse

label order:

    show radik smile c with dissolve

    radik 'Праальный выбор, дружище, щас всё сделаю.'

    hide radik with Dissolve(1)

    'Спустя пять минут нам принесли наш заказ.'

    show shava with dissolve

    ''

    hide shava with dissolve
    show alla confused with dissolve

    alla 'Бррр, меня сейчас стошнит.'

    'Недолго думая, я сделал глубокий вдох, зажмурился и откусил сей кулинарный шедевр.'

    euklid 'На вкус это намного лучше, чем на вид.'

    hide alla with fastdissolve
    show semen smile with dissolve

    semen 'Во, я же говорил.'

    hide semen smile with fastdissolve
    show alla angry with dissolve

    alla 'Вы оба просто отвратительны…'

    'Когда мы доели наши блюда, пришло время прощаться с моими новоиспеченными друзьями.'

    hide alla angry with fastdissolve
    show semen smile with dissolve

    semen 'Теперь будем ходить сюда каждый день после пар.'

    hide semen smile with fastdissolve
    show alla 1_ with dissolve

    alla 'Ну как-нибудь без меня… Саша, с тобой всё хорошо? Ты какой-то бледный.'

    euklid 'Всё в поря…'

    stop music fadeout 1.0

    show alla amazed with dissolve

    'Внезапно я ощутил острую боль в районе живота, я не смог стоять на ногах и упал на землю.'

    show alla sad 0_1 with dissolve

    alla 'САШААААА, НЕТ.'

    window hide
    $ _dismiss_pause = False
    play sound ambulance
    scene black_background with Dissolve(3)
    scene 1end1 with dissolve
    scene 1end2 with Dissolve(2)
    $ renpy.pause(5, hard=False)

    return

label order_refuse:

    euklid 'Алла права, не хочу снова оказаться в больнице.'

    semen_s smile 'Ну смотрите, если будете просить меня кусочек, я вам откажу.'
 
    'Прошло пару минут, Семёну принесли его долгожданное блюдо.'

    hide radik smile c with dissolve
    show shava with fastdissolve

    ''

    hide shava with fastdissolve
    show alla amazed with dissolve

    alla 'Как ты это ешь?'

    hide alla amazed with fastdissolve
    show semen laugh with dissolve

    semen 'С большим удовольствием.'

    'Подождав, пока Семён доест сей кулинарный шедевр, мы вышли на улицу и попрощались.'

    scene guk with fade

    show semen smile with dissolve

    semen 'До завтра, ребятки.'

    euklid 'Пока, друг.'

    show semen usual with dissolve

    stop music fadeout 1.0

    'Семён остановился и уставился на меня.'

    show semen sus with dissolve

    semen 'Ты никогда меня так не называл… Да что с тобой такое.'

    'Чёрт, этот чудик постепенно всё понимает, надо что-то с этим делать.'

    hide semen with fastdissolve
    show alla angry with dissolve

    alla 'Семён, отстань от него, только не начинай строить свои теории заговора на пустом месте.'

    alla 'Ты в прошлом году так преподавателя по английскому обвинил в том, что он рептилия, так бедному человеку пришлось уволиться из-за насмешек, а тебя с тех пор все шизиком считают.'

    hide alla angry with fastdissolve
    show semen amazed with dissolve

    semen 'Но он действительно себя подозрительно вёл.'

    hide semen amazed with fastdissolve
    show alla smile 3 with dissolve

    alla 'Всё, прощай.'

    'Девушка взяла меня за руку и повела за собой'

    hide alla smile 3 with dissolve

    'В этот раз ему повезло, но в следующий я точно сотру ему память.'

    scene black_background with fade

    'Так прошло несколько недель с тех пор, как я занял тело человека по имени Саша.'

    'Должен признаться, ходить на пары мне очень понравилось, также я немного сдружился с Аллой и Семёном.'

    'Так непривычно испытывать те чувства, которых у тебя раньше не было.'

    alla 'Саша, ты чего опять в облаках? Сейчас будет пара со Святогором Великановичем, готовься.'

    scene aud with dissolve

    euklid 'Интересно, что он на этот раз придумает.'

    show teach smile 2 with dissolve

    teacher 'Хай, молодёжь! Сегодня у меня для вас есть кое-что особенное, можно сказать {i}хайповое{/i}!'

    show teach sad with fastdissolve

    play sound cricket
    $ _dismiss_pause = True
    $ renpy.pause(2.35, hard=False)
    $ _dismiss_pause = False

    semen_s smile 'Он опять за старое…'

    alla_s smile 2 'Я уже привыкла.'

    show teach smile 2 with fastdissolve

    teacher 'Для начала мы немного поизучаем новую тему, которая нам сегодня пригодится.'

    show teach smile with fastdissolve

    teacher 'Тема нашего сегодняшнего обсуждения -  шифрование! Кто сможет мне рассказать про шифрование?'

    play music para fadein 3.0

    show teach sad with fastdissolve

    'Семён сразу же поднял руку.'

    show teach smile 2 with fastdissolve

    teacher 'Ух ты, вновь вы, Семён, отвечайте!'

    show teach sad with fastdissolve

    semen_s smile 'Шифрование - это обратимое преобразование информации в целях её сокрытия от неавторизованных лиц.'

    semen 'Важной особенностью любого алгоритма шифрования является использование ключа, который утверждает выбор конкретного преобразования для данного алгоритма.'

    show teach smile 2 with fastdissolve

    teacher 'Замечательный ответ, как всегда хорошо, Семён.'

    show teach smile with fastdissolve

    teacher 'Но сегодня мы не будем глубоко погружаться в эту тему, определение вам уже известно.'

    show teach smile 2 with fastdissolve

    teacher 'Сейчас мы рассмотрим несколько методов шифрования, после чего я дам вам работу.'

    show teach sad with fastdissolve

    'Этот Семён явно умён, не хотелось бы, чтобы он был помехой на моём пути.'

    show teach smile 2 with fastdissolve

    teacher 'Начнём с такого стандартного метода как ROT32.'

    scene rot_ with dissolve

    teacher 'Этот шифр известен многим детям. Ключ прост: каждая буква заменяется на предыдущую за ней в алфавите.'

    scene letter_ with dissolve

    teacher 'Так, Я заменяется на Ю, Ю - на Э, и т.д. Фраза "Типичный программист" - это "Сзозцмъи опнвпяллзрс".'
      
    scene alphabet_ with dissolve
    
    teacher 'Попробуйте расшифровать сообщение: "лдвяаяис"'

    scene alphabet
    show teach smile 2

    show teach sad with fastdissolve

label start8:

    $ phrase = renpy.input('Попробуйте расшифровать сообщение: "лдвяаяис"', length = 20).strip()

    if phrase == 'мегабайт' or phrase == 'Мегабайт' or phrase == 'МЕГАБАЙТ':

        hide podskazka1 with dissolve
        'Отлично! У вас получилось расшифровать сообщение!'

    elif bit >=3:
        jump start81

    else:
        'Попробуйте еще раз'
        if bit >=1:
            show podskazka1 with dissolve
        $ bit +=1
        jump start8

label start81:

    scene trans_ with dissolve

    teacher 'Шифр транспортирования у нас идёт далее.'

    teacher 'В транспозиционном шифре буквы переставляются по заранее определённому правилу.'

    scene hello with dissolve

    teacher 'Например, если каждое слово пишется задом наперед, то из "hello world" получается "dlrow olleh".'

    scene hello2 with dissolve

    teacher 'Другой пример — менять местами каждые две буквы. Таким образом, "hello world" станет "eh ll wo ro dl".'

    show hello3 with dissolve

    teacher 'Ещё можно использовать столбчатый шифр транспортирования, в котором каждый символ написан горизонтально с заданной шириной алфавита, а шифр создаётся из символов по вертикали.'

    teacher 'Ну вот эти 2 метода и будут использоваться в работе, которую вы сейчас получите.'

    scene alphabet_ with dissolve

    euklid 'Ну, звучало это не сложно, надеюсь и тесты будут простыми.'

    'Вернувшись на своё место, я начал изучать тест.'
    
    euklid 'Тут всё как он и говорил, выглядит не сложно.'

    $ phrase = renpy.input('Вот и первое задание: "Расшифруйте следующий текст: Пягзнуяй"', length = 9).strip()

    if phrase == 'радиофак' or phrase == 'Радиофак' or phrase == 'РАДИОФАК':

        euklid 'Вроде получилось, хе.'

    else:

        euklid 'Вот блин, я не тот символ вписал, грх, ну ладно. Так, что же там дальше...'

    scene test1 with dissolve
        
    euklid 'Второе задание: "Расшифруйте следующий текст: " Вот это скачок в сложности, такс, ну ладно, посмотрим, как тут ответить.'

    $ phrase = renpy.input('Расшифруйте следующий текст и запишите ответ на русском через пробел маленькими буквами: ', length = 28).strip()

    if phrase == 'Информационная безопасность' or phrase == 'Информационнаябезопасность' or phrase == 'Информационная безопасность' or phrase == 'Информационная_безопастность' or phrase == 'информационная Безопасность' or phrase == 'ИнформационнаяБезопасность' or phrase == 'Информационная_Безопастность' or phrase == 'ИНФОРМАЦИОННАЯ БЕЗОПАСНОСТЬ' or phrase == 'ИНФОРМАЦИОННАЯБЕЗОПАСНОСТЬ' or phrase == 'ИНФОРМАЦИОННАЯ_БЕЗОПАСНОСТЬ':

        euklid 'Да уж, это заняло чуть больше времени чем я ожидал.'

    else:
        euklid 'Да что же это такое, случайно не там пробел поставил.'

    scene test2 with dissolve

    euklid 'Третье задание: "Расшифруйте следующий текст и запишите ответ на русском:"'

    $ phrase = renpy.input('Расшифруйте следующий текст и запишите ответ на русском через пробел маленькими буквами:', length = 28).strip()

    if phrase == 'Транспортный шифр' or phrase == 'транспортный шифр':
        
        'Алла посмотрела в мою работу и списала пару ответов.'

        alla 'Саша, да ты ювелир… Столько правильных ответов.'

    else:

        euklid 'Вот чёрт, надо будет повторить эту тему дома.'

label start9:

    scene aud2 with dissolve

    'Я посмотрел на лист с обеих сторон.'

    'На задней стороне было четвертое задание с какими-то точками и чёрточками.'

    $ phrase = renpy.input('Расшифруйте следующий текст и запишите ответ на русском: ".-. - ..-. --..-- / ..- .-. ..-. ..- --..-- / .--. --- .--. --- .--"', length = 28).strip()

    if phrase == 'РТФ УРФУ ПОПОВ':

        euklid 'Жаль, что далеко не все поймут в чём же дело. Действительно тонко, не так уж много образованных радистов в наше время, кто знает почему это так интересно и необычно.'
        
    else:
        euklid 'Что это за шуточки? Это вообще имеет смысл? Так я и поверил, ну и бредятина.'

    'Сдав тест, я отправился к мужскому туалету, чтобы связаться с Сигмусами.'

    scene toilet_ with fade

    'Я набрал номер секретаря Автократа... Жаль, что в межгалактическом роуминге надо платить на 40 рублей больше за минуту звонка.'

    play sound aliena

    sec 'Слушаю вас.'

    euklid 'Это Евклид, хочу доложить, что миссия на планете Земля протекает гладко, но я ещё не определил местонахождение волшебного камня.'

    play sound alienb

    sec 'Евклид, это вы! Как вовремя! Наши спутники сумели найти координаты камня, я отправлю их на ваш e-mail.'

    euklid 'Давайте лучше на урфушную почту.'

    play sound alienc

    sec 'Нет. Кстати, по нашим данным вы уже обладаете {i}необходимой информацией{/i} для взлома камня.'

    play sound aliend

    sec 'Империя рассчитывает на вас, постарайтесь не подвести наше доверие.'

    euklid 'Вот сухарь.'

    scene toilet_2 with dissolve

    'Выйдя из кабинки туалета, я направился к выходу.'

    stop music fadeout 1.0

    show semen sus with dissolve

    'Вдруг, Семен выскочил из соседней кабинки и перекрыл мне выход.'

    semen 'Вот ты и попался.'

    euklid 'Семён, ты всё не так понял. Позволь я объясню.'

    show semen angry with dissolve

    semen 'Что я не так понял? Я уже давно начал тебя подозревать, ты очень странно себя вёл с того момента, как очнулся.'

    menu:

        'Как поступить?'

        'Рассказать правду':
            jump truth

        'Соврать':
            $ truth = False
            jump lie

label truth:

    euklid 'Ладно, нет смысла отпираться, я всё расскажу.'

    semen 'Да уж расскажи, Саша, или как там тебя зовут на самом деле.'

    euklid 'Меня зовут Евклид, я не человек, а представитель расы Сигмусов.'

    euklid 'Я попал в тело Саши, чтобы получить данные волшебного камня, который находится в здании этого института.'

    show semen sus angry with dissolve

    semen 'Так ты захватчик?'

    euklid 'На самом деле да... Но честно, я не хочу, чтобы с этой планетой случилось что-то плохое.'

    show semen angry with dissolve

    semen 'Не рассказывай мне сказки.'

    euklid 'Нет, я правда не планирую ничего плохого, поверь мне...'

    show semen sus with dissolve

    'Парень окинул меня подозрительным взглядом.'

    semen 'Ну допустим. Тогда зачем тебе эти данные?'

    euklid 'Я обязательно расскажу тебе о них позже, а сейчас мне надо идти.'

    scene black_background with fade

    'Я быстро выбежал из туалета, оставив Семёна в недоумении.'

    play sound door_close 
    $ _dismiss_pause = False
    scene black_background with Dissolve(1)
    window hide
    show deystv with wiperight
    $ _dismiss_pause = True
    $ renpy.pause(3, hard=False)
    jump start10

label lie:

    euklid 'Ну вот, ты сам ответил на свой вопрос.'

    euklid 'Я только недавно пришёл в себя, вот и причина такому поведению. Люди после такого бывает и память теряют, так что я ещё легко отделался.'

    show semen sus angry with dissolve

    semen 'Тогда что насчёт того, что ты говорил в туалете?'

    euklid 'Так я готовлюсь к конкурсу студентов и учу свою роль.'
   
    show semen amazed with dissolve

    semen 'Ё-моё, точняк, через неделю же «Студент года». Прости, чувак, зря я тебя обвинил.'

    euklid 'Да ничего страшного, ха-ха.'

    euklid 'Ой, смотри время уже 15:40! Через двадцать минут закрывается «Шаурма у Радика».'

    semen 'Вот блин, совсем забыл.'

    show semen smile with dissolve

    semen 'Ладно, Саня, увидимся завтра, я побежал.'

    hide semen smile with dissolve

    scene black_background with fade

    'Парень быстро ретировался, а я спокойно вышел из туалета.'

    play sound door_close 
    $ _dismiss_pause = False
    scene black_background with Dissolve(1)
    window hide
    show deystv with wiperight
    $ _dismiss_pause = True
    $ renpy.pause(3, hard=False)


    jump start10

label start10:

    $ _dismiss_pause = False

    scene black_background with fade

    window show

    'Сейчас или никогда. Надо скорее найти этот камень.'

    'Я открыл сообщение, отправленное секретарём. Запомнив координаты места, я двинулся в путь.'

    euklid 'Так, а сейчас направо...'

    'Спустя некоторое время я дошёл до лестницы, ведущей в подвал.'
    
    play music scary volume 1.15
    scene ladder with fade

    menu:

        'Как поступить?'

        'Не спускаться':
            jump ndown

        'Спуститься':
            jump down

label ndown:

    euklid 'Ну уж нет!'

    'Развернувшись, я пошёл в обратном направлении.'

    scene black_background with dissolve

    play sound autokrat_exo

    autokrat 'Евклид, не забывай своё предназначение. Империя рассчитывает на тебя. \n Евклид, не забывай своё предназначение. Империя рассчитывает на тебя.'

    'Повторяющиеся слова опять звоном раздались в моей голове.'

    scene ladder with fade

    'Я понял, что мне просто так не дадут свернуть назад. Я снова направился к лестнице в подвал'

    jump down

label down:

    'Спустившись вниз, я оказался в длинном тёмном коридоре'

    scene corridor with fade

    'Вдалеке виднелась единственная дверь, я направился к ней.'

    'На удивление она была открыта, будто бы кто-то уже ожидал меня там.'

    scene cabinet with fade

    'Зайдя внутрь, я попал в просторный кабинет, в котором сильно пахло затхлостью и плесенью.'

    euklid 'Так, по координатам камень находится где-то тут.'

    menu:

        'Где искать?'

        'На столе':
            jump ontable

        'Под столом':
            jump undertable

label ontable:

    'На столе лежали кипы книг, старых газет и учебников'

    'Учебник «1000 и 1 строчка кода», учебник «Шифрование для хлебушков», книга «Как кодили в Древней Руси» и куча подобной литературы.'

    'В одной из подобных книг была записка.'

    show note1 with dissolve

    euklid 'Что за ерунда...'

    hide note1 with dissolve

    jump start11

label start11:

    menu:

        'Где искать?'

        'На столе':
            jump ontable_

        'Под столом':
            jump undertable

label ontable_:

    'Я зря теряю время.'

    jump start11

label undertable:

    'Под столом стояла мусорная корзина с остатками еды и исписанными бумагами.'

    'Превозмогая жуткое отвращение, я засунул туда руку. Немного покопавшись, я нащупал свёрнутый листок.'

    show note2 with dissolve

    'Это может быть полезным.'
    hide note2 with dissolve

    menu:

        'Где искать?'

        'В комоде':
            jump commode

        'В шкафу':
            jump closet

label commode:

    'В комоде, кроме старых однотипных рубашек, ничего не было.'
    jump start12

label start12:

    menu:

        'Где искать?'

        'В комоде':
            jump commode_

        'В шкафу':
            jump closet


label commode_:

    'Там я уже смотрел. Камнем даже и близко не пахнет.'

    jump start12

label closet:

    'Порывшись в шкафу, я нашел тяжёлый металлический сейф.'

    show screen safe_code with dissolve

label start133:
    show note22 with dissolve
    euklid 'Хмм, нужен четрыхзначный код.'

label start13:

    play sound opensafe
    show open safe with dissolve
    hide note22 with fastdissolve
    euklid 'О, получилось!'

    hide open safe with fastdissolve

    show note3 with dissolve

    'Но вместо волшебного камня в сейфе лежала ещё одна записка.'

    hide note3 with dissolve

    'Вдруг я почувствовал сильную боль в области затылка. В глазах потемнело, я упал на пол.'

    stop music
    play sound fall2

    scene black_background with dissolve
    pause 2

    'Евклид, вставай, ты уже опаздываешь на космический корабль.'

    'Сынок, это твой шанс привлечь внимание Великого императора! Кто знает, может тогда ты наконец-то сможешь не голодать и жить счастливо.'

    euklid 'Мама!? Ты жива?'

    'Я так долго не слышал этот голос, который был мне дороже всего на свете.'

    'Прости сынок, мне пора. Вставай, ты должен бороться!'

    euklid 'Постой!'

    pause 2

    'Я открыл глаза...'

    window hide

    scene jail teacher sad with Dissolve(2)

    window show

    'Передо мной была решётка, за ней у большого стола стоял тот, кто ударил меня по затылку.'

    euklid 'Ну здравствуйте, Святогор Великанович.'

    scene jail teacher with fastdissolve

    teacher 'Конечно, дорогой, на своём веку я повидал много таких как ты. Охотой на инопланетных ящеров занимался ещё мой дед, а до него его дед, а до него...'

    euklid 'Да понял я, можете не продолжать.'

    teacher 'Тогда ты понимаешь, что я сделаю с тобой?'

    euklid 'Мирно отдадите волшебный камень?'

    scene jail teacher sad with fastdissolve

    teacher 'Хо-хо-хо, а ты забавный. Язык тебе отрежу в самую последнюю очередь.'

    euklid 'Я не шучу, отдайте его лучше по-хорошему.'

    'Недалеко от клетки на полу лежали ключи, надо как-то отвлечь старика, чтобы попытаться до них достать.'

    teacher 'Камень не отдам, но коль меня рассмешил – дам посмотреть.'

    scene jail with dissolve

    'Мужчина ненадолго отошёл, вернувшись уже с магическим камнем.'

    play music anxiety

    scene jail cum with dissolve

    teacher 'Хо-хо-хо, сейчас всё узнаешь.'

    'Он медленно подошёл крешетке и замахулся.'

    if truth == True:
        jump delta_truth
    else:
        jump delta_lie

label delta_truth:

    alla_s amazed 'Остановитесь!'

    'В комнату вбежали Алла и Семён.'

    alla_s amazed 'Что вы творите, Святогор Великанович!?'

    teacher 'Ну вот, только этого мне не хватало. Молодые люди пройдите обратно в кабинет, позже я вам всё объясню.'

    alla_s angry 'Я никуда без него не уйду!'

    'Девушка показала пальцем на меня.'

    teacher 'Что за головная боль...'

    scene jail with dissolve

    'Пока Алла отвлекала преподавателя, я дал знак Семёну, чтобы он кинул мне ключи.'

    semen_s angry 'Святогор Великанович, он хочет сбежать. Я уведу Аллу, а вы сделайте с ним то, что хотели.'

    alla_s amazed 'Что ты такое говоришь, Семён?'

    semen_s angry 'Пошли отсюда.'

    'Он уволок рыдающую девушку за собой. Мы остались один на один с профессором.'

    teacher_s 'А он умный малый, получит у меня автомат на экзамене. Ну что продолжим то, что начинали...'

    window hide
    $ _dismiss_pause = False
    stop music fadeout 3.0
    scene black_background with Dissolve(3)
    scene 1end1 with dissolve
    scene 2end2 with Dissolve(2)
    $ renpy.pause(5, hard=False)
    return 

label delta_lie:

    alla_s amazed 'Остановитесь!'

    'В комнату вбежала испуганная Алла.'

    alla_s angry 'Что вы творите, Святогор Великанович!?'

    teacher 'Ну вот, только этого мне не хватало. Алла, пройдите обратно в кабинет, позже я вам всё объясню.'

    alla_s angry 'Я никуда без него не уйду!'

    'Девушка показала пальцем на меня.'

    teacher 'Что за головная боль...'

    scene jail with dissolve

    'Пока Алла отвлекала преподавателя, я попытался достать до ключей. Алла увидела краем глаза мои безуспешные старания и незаметно пнула ключи в мою сторону.'

    alla_s angry 'Да что вы творите, я сейчас позвоню в полицию!'

    teacher_s 'Пока полиция доедет, я успею расправиться с вами двумя.'

    scene black_background with fade
    play sound key

    'Я быстро открыл засов решётки и выбежал к Алле.'
    
    scene dungeon1 with fade

    euklid 'Не трогайте её!'

    scene dungeon12 with dissolve

    teacher 'Ах, как ты сумел сбежать? Ну сейчас вы у меня попляшите.'

    scene dungeon1 with dissolve

label start14:

    menu: 
        'Надо срочно что-то делать.'
        
        'Ударить в живот':
            jump stomach

        'Ударить по голове':
            jump head

label stomach:

    'Я быстро ударил профессора в живот, он потупился назад, но продолжал стоять на ногах'
    jump start16

label head:

    'Я замахнулся, чтобы ударить его по голове, но он быстро перехватил мою руку и первым сделал удар.'
    jump start15

label start15:

    menu: 
        'Надо срочно что-то делать.'
        
        'Ударить в живот':
            jump stomach

        'Ударить по голове':
            jump head_

    
label head_:
    'Нельзя! Он готов к этой атаке!'
    jump start15

label start16:

    menu:
        'Так теперь надо сделать следующий ход.'

        'Оглушить':
            jump stun

        'Сбежать с Аллой':
            jump runout

label stun:

    scene upal with Dissolve(1)

    'Я успешно совершил удар, пока он без сознания надо забрать камень.'

    scene upal2 with dissolve
    
    'Я взял в руки камень, передо мной всплыло послание.'
    jump start18

label runout:

    'Я взял девушку за руку и попытался выбежать из подвала, но профессор быстро пришёл в себя и вновь ударил меня.'
    jump start17

label start17:

    menu:
        'Что мне делать?'

        'Оглушить':
            jump stun

        'Сбежать с Аллой':
            jump runout_

label runout_:
    'Мне кажется, это не лучшая идея'
    jump start17

label start18:

    scene alph2 with dissolve

    $ phrase = renpy.input('Расшифруйте послание: ', length = 8).strip()

    if phrase == 'ИНФОБЕЗ' or phrase == 'инфобез' or phrase == 'Инфобез' or lastPosl >= 5:

        scene dungeon2 with Dissolve(1)

        scene dungeon3 with Dissolve(1)

        'Вдруг камень ярко засиял. Передо мной начали появляться терабайты свежей информации.'

        jump start19

    else:
        $ lastPosl += 1
        euklid 'Да как же оно расшифровывается!?'
        jump start18

label start19:

    scene dungeon4 with dissolve

    euklid 'Наконец-то у меня получилось!'
    '...'

    scene dungeon5 with dissolve

    show alla angry very with dissolve

    alla 'Ну и как ты мог пойти в такое опасное место совершенно один?'

    euklid 'Постой, Алла, для начала я хотел тебе в кое-чём признаться.'

    show alla 1_ with dissolve

    stop music fadeout 1.0

    play music fire volume 0.75

    alla 'Я всё знаю.'

    euklid 'Я понимаю, что ты будешь злиться... Стоп ЧТО!? Откуда?'

    alla 'Я не глупая, мне давно стало всё понятно.'

    euklid 'Но почему ты продолжала со мной общаться?'

    alla 'Сначала хотела тебя поймать непосредственно на месте преступления, а потом....потом...'

    show alla confused_ with dissolve

    'Девушка сильно покраснела и начала запинаться.'

    alla 'Саша, ой то есть...'

    euklid 'Моё настоящее имя Евклид, называй меня так.'

    alla 'Хорошо, Евклид, что ты теперь собираешься делать?'

    euklid 'Полечу обратно на свою планету, а что?'

    show alla happy_ with dissolve

    alla 'Ну не хотел бы ты остаться тут? Ты хороший студент, тебя ждёт перспективное будущее.'

    euklid 'Но у меня на Земле никого нет.'

    alla 'У тебя есть я.'

    show alla 4 with dissolve

    'Девушка кокетливо улыбнулась и взяла мою руку.'

    menu:
        'Как поступить?'

        'Остаться на Земле':
            jump zeml
        'Вернуться к Сигмусам':
            jump sigma

label zeml:
    
    euklid 'А знаешь, идея не такая уж плохая.'

    play music good_end fadein 0.5

    show alla 5 with dissolve

    'Я крепко обнял девушку.'

    show alla 6 with dissolve

    alla 'Евклид, а почему от тебя пахнет так, как будто бы ты рылся в мусоре?'

    euklid 'Это долгая история...'

    window hide
    $ _dismiss_pause = False
    stop music fadeout 2.0
    scene black_background with Dissolve(2)
    scene text1 with dissolve
    $ _dismiss_pause = True
    $ renpy.pause(14, hard=False)
    scene black_background with Dissolve(1)
    scene the end with Dissolve(2)
    $ renpy.pause(1, hard=True)
    scene the end 3 with Dissolve(2)
    $ renpy.pause(5, hard=False)
    return 

label sigma:

    euklid 'Прости, но я так не могу. Я возвращаюсь обратно, это мой долг.'

    show alla 1_ with dissolve 

    alla 'Я всё понимаю, тогда прощай...'

    show alla 9 with dissolve

    euklid 'Прощай...'

    scene black_background with Dissolve(2)

    'Я связался с секретарём Сигмусов и попросил отправить меня обратно, так как я выполнил миссию. Первым делом я отправился к Автократу.'

    scene autokrat_scene with fade
    play music dark

    euklid 'Да здравствует его величество Великий император Автократ!'

    autokrat 'Здравствуй, Евклид.'

    autokrat 'Ну ты меня порадовал, наконец-то вся информация о Земле у нас, теперь мы сможем поработить эту планету.'

    menu:
        'Убедить Автократа не захватывать Землю':
            jump convince

        'Молча согласиться':
            jump agree

label convince:

    euklid 'Великий император, позвольте заметить, что гораздо лучше будет не захватить Землю, а сотрудничать с её жителями.'

    autokrat 'Что ты несёшь?'

    euklid 'Я пробыл на Земле достаточно, чтобы понять, что там живут очень умные и хорошие люди. Поверьте, если использовать нашу силу и их ум, то нашу расу ждёт только светлое будущее.'

    autokrat 'Мне стоит обдумать твоё предложение.'

    window hide
    $ _dismiss_pause = False
    stop music fadeout 2.0
    scene black_background with Dissolve(2)
    scene text2 with dissolve
    $ _dismiss_pause = True
    $ renpy.pause(8, hard=False)
    scene black_background with Dissolve(1)
    scene the end with Dissolve(2)
    $ renpy.pause(1, hard=True)
    scene the end 4 with Dissolve(2)
    $ renpy.pause(5, hard=False)
    return 

label agree:

    'Автократ подозвал своего секретаря.'

    autokrat 'Немедленно начинаем вторжение!'

    window hide
    $ _dismiss_pause = False
    stop music fadeout 2.0
    scene black_background with Dissolve(2)
    scene text3 with dissolve
    $ _dismiss_pause = True
    $ renpy.pause(5, hard=False)
    scene black_background with Dissolve(1)
    scene the end 55 with Dissolve(2)
    $ renpy.pause(1, hard=True)
    scene the end 5 with Dissolve(2)
    $ renpy.pause(5, hard=False)
    return 

# Without Fire wood-burning stove simulator

Without Fire is a wood-burning stove simulator that aims to replicate in part the look, sounds, scent, and feel of a real stove. The motivation for this project was to help households with woodburners reduce air pollution while still enjoying their stove (or fireplace). It is based around a Raspberry Pi computer, and this repository includes full details to let you replicate it (and improve it!) yourself.

## Background

Domestic burning, including in wood burning stoves, is the [biggest source of harmful PM 2.5 emissions in the UK](https://www.gov.uk/government/statistics/emissions-of-air-pollutants/emissions-of-air-pollutants-in-the-uk-particulate-matter-pm10-and-pm25). The top reason for domestic burning is "to create a homely feel", with almost half of respondents to a UK survey citing this reason [(this PDF, p86)](http://randd.defra.gov.uk/Document.aspx?Document=14972_Finalreport-BurninginUKhomesandgardens.pdf). My aim with this project was to try to recreate as much of the homely feel of a wood fired stove as possible, without the emissions. Moreover, I wanted the solution to be retrofittable into existing stoves. There are plenty of options on the market for [electric stoves](https://www.directstoves.com/stoves/electric-stoves.html), but a small but significant proportion ([7.5%](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/517572/Summary_results_of_the_domestic_wood_use_survey_.pdf)) of UK homes already have some wood burning capability and may want to continue using it to some extent. Others may have a fireplace where they are thinking of installing a stove, and they could try this as an alternative. 

## Materials

I've provided links to new items but many can be sourced second-hand on Ebay.
<ul>
    <li>Fundamental:<ol style="list-style-type: circle;">
            <li>Raspberry Pi computer with power supply. I used my Pi 3 Model B which had 4 USB ports, but can also be made with a Zero [I will note adaptations for this where appropriate].</li>
        </ol>
    </li>
    <li>For light:<ol style="list-style-type: circle;">
            <li><a href="https://shop.pimoroni.com/products/unicorn-hat-mini">Pimoroni Unicorn HAT Mini</a> (LED matrix) for the firelight.</li>
            <li>An empty 1 pint plastic milk bottle to contain the Pi/HAT and act as a diffuser for the light.</li>
        </ol>
    </li>
    <li>For sound:<ol style="list-style-type: circle;">
            <li>Speaker(s). These can be USB-powered with standard audio jack, or <a href="https://thepihut.com/products/mini-external-usb-stereo-speaker">USB audio</a>. Better sound quality is better but don't break the bank.</li>
            <li>If you use speakers with an audio jack, a <a href="https://thepihut.com/products/usb-audio-adapter-works-with-raspberry-pi">USB audio adaptor</a> is recommended to avoid hum.</li>
        </ol>
    </li>
    <li>For scent:<ol style="list-style-type: circle;">
            <li>USB aroma diffuser like <a href="https://www.ebay.co.uk/itm/173506521449">this</a>, a <a href="https://www.ebay.co.uk/itm/251088085968?_trkparms=ispr%3D5&hash=item3a760423d0">USB extension cable</a>, and small bottle of woodsmoke essential oil similar to <a href="https://nikura.com/products/firewood-pure-essential-oil-blend-aromatherapy-100-natural">this</a> (although it is a bit perfumey).</li>
        </ol>
    </li>
    <li>For heat:<ol style="list-style-type: circle;">
            <li>A <a href="https://www.ebay.co.uk/itm/273412280854">~200W ceramic bulb</a> (used for heating reptiles), <a href="https://www.amazon.co.uk/Himifuture-Holder-Ceramic-Heater-Bracket/dp/B08MYFZZHT/ref=sr_1_5?keywords=ceramic+bulb+holder&qid=1644258674&sr=8-5">porcelain (heat proof) bulb holder</a>, and something to attach it to (this is to provide radiant heat like you get from a stove at a relatively low power consumption). &nbsp;</li>
        </ol>
    </li>
</ul>

## Raspbery Pi setup

It will be easiest to use a &ldquo;headless&rdquo; setup to avoid the need to connect a keyboard/screen to the Pi. Andy Brace has some very clear instructions for how to do this <a href="https://github.com/openbook/shouldi-eink-display/blob/main/README.md">here</a> (steps 1-3).

## Light

A Unicorn HAT Mini LED matrix is used to create a flickering orange light that resembles firelight. The program is set up in such a way that the light flickers more slowly, and becomes more red and slightly dimmer over time, similar to a real fire. After a semi-random period (around 30 mins) it flickers back into life, like a new log has been put on.
<ol>
    <li>First install the Unicorn HAT Mini by following <a href="https://learn.pimoroni.com/article/getting-started-with-unicorn-hat-mini">these instructions</a>. Check that it is working by navigating to the &ldquo;examples&rdquo; folder and running some of the programs in it.</li>
    <li>Now clone this (i.e. Without Fire) repository from GitHub to your pi (in the command line type &ldquo;git clone https://github.com/mikefsway/withoutfire.get&rdquo;. You may need to move the newly created folder &ldquo;withoutfire&rdquo; into the Pimoroni folder on your Pi for it to run properly. E.g. by running &ldquo;mv /home/pi/withoutfire /home/pi/Pimoroni&rdquo;.</li>
    <li>Run the file withoutfire.py (&ldquo;python withoutfire.py&rdquo;). The Unicorn HAT Mini should light up in a way that resembles flickering firelight.</li>
    <li>To protect this setup and diffuse the bright/directional LED light, crush a one pint plastic milk bottle flat, cut a slit in the side, and place the Pi (with HAT) inside. You can already place this in your stove and run the program, and should start to resemble glowing firelight. Ultimately you can add logs around it for a more realistic effect, but there are more steps to go through first if you want to set up the sound and other elements.</li>
    <li>The withoutfire.py file is commented in some detail to indicate which settings you can tweak.</li>
</ol>

![Image of Pi in milk bottle](/images/bottle.png?raw=true)

## Sound
When withoutfire.py runs, it also plays a sound file on a ~5 minute loop. Similar to the light, this becomes quieter over a period of around 30 minutes, simulating a real fire burning down. The sound file used is an edited version of a <a href="https://freesound.org/people/petebuchwald/sounds/496130/">fireplace recording by petebuchwald</a> available on freesound.
I've included three versions of the sound file. One has quite quiet crackles relative to the background hiss of the stove, and two with increasingly loud crackles. The version that plays can be changed in the withoutfire.py file. Choose the version that sounds best on your speaker setup.

It is best to avoid using the audio jack on the Pi itself (this isn't even an option if you are using a Pi Zero). The Unicorn HAT creates a lot of electrical hum. One option is to use a USB speaker like the one available from the Pi Hut linked above &ndash; although note the sound quality isn't amazing. The fire effect is *much better* with a better speaker, with a bit more bass. Even reasonable computer speakers are quite good. For my setup I use a USB audio adaptor (see link above). Some helpful guidelines on how to get a USB audio interface working are available [here](https://www.raspberrypi-spy.co.uk/2019/06/using-a-usb-audio-device-with-the-raspberry-pi/). 

I originally had a pair of speakers, but actually cut one of them off to make it easier to pack the whole setup away. I didn't feel too bad about this as they were cheap second hand ones from Ebay!
You could also use a Bluetooth speaker.

## Scent

This is an interesting one, and I'm still not completely sold on it. I picked up a cheap USB-powered aroma oil diffuser, and it comes on automatically with the Pi. I've taped it to the back of the speaker for ease of setup/stowing. It has a setting to release scent once a minute. The scent I've found so far (linked above) is quite nice but a bit like a Scandinavian spa. I'd like to find something that is more like just wood smoke. Maybe you can find something better.

![Image of speaker and scent diffuser](/images/speaker.png?raw=true)

## Heat

Obviously one of the main functions of a stove is to provide heat. They are notable from providing particularly high radiant heat as the fire/surface gets so hot. Unfortunately, providing high radiant heat electrically requires either a high powered resistance heater, or possibly an infrared panel heater (which are quite expensive). The solution I'm trying out is to use a 200W ceramic bulb intended for heating reptile tanks. It won't be any good for heating a room, but if you position it close enough in theory it should provide a feeling of warmth on the skin. Unfortunately the inverse square law means you need to be pretty close to it to get this effect &ndash; e.g. mounting it on a coffee table pointing at you. Clearly you should not touch the bub itself as it gets very hot. &nbsp;

## Final setup

Place the Pi (in milk bottle) in the stove, a stack logs around it in a realistic manner. I find having some smaller sticks across the bottle to break up the shape helps create a more realistic illusion. I've done my best to check the temperature the setup gets to and haven't experienced it becoming warm (let along hot), but clearly this is a risk you should pay attention to.

![Image of device in stove](/images/kindling.png?raw=true)

In our stove the door can be closed with the cables for the Pi power, audio, etc. emerging from it. The speaker(s) can be hidden away to the side if possible, and you may like to use tape to cover any annoying power lights.
I use cron to run the script automatically on startup. You do this by entering &ldquo;crontab &ndash;e&rdquo;, then adding the following line to the end of the file: &ldquo;@reboot python /home/pi/Pimoroni/withoutfire/withoutfire.py&rdquo; (or whatever the path on your system is).

## Final thoughts and next steps

I've been using the simulator a lot since setting it up. Obviously it doesn't look as good as a real fire with proper flames. But it is really nice to have ticking away in the background with the lights dimmed. It is also really handy to be able to turn in on for short periods.

Things I would like to improve about the project:
- While the milk bottle is effective and a good re-use option, I'd like to come up with something that looks a but sleeker. I'm experienting with alternatives and will update.
- If I had a battery pack, I'd be interested to see how long it could operate on a single charge. This would avoid the need for there to be a plug socket near to the stove. 
- It would be great to introduce an element that replicates actual flames or smoke. There are commercial options available, which I think use a similar technology to the nebuliser in the oil (scent) diffuser. But I haven't had a chance to play with this yet, and obviously you would need to be careful about creating water vapour inside the stove.
- It could be interesting to work on something that indicates when weather conditions are worse for air pollution, making it especially bad to use a stove and recommending the use of the simulator instead.

![Image of device working](/images/glowing1.png?raw=true)

![Image of device working](/images/glowing2.png?raw=true)

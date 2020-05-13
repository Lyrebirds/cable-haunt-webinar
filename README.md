# cable-haunt-webinar

Dette er vores git repository med alt materiale nødvendigt til ida's webinar om cablehaunt.

Dette repo inderholder den modem firmware vi vil bruge under webinaret samt de tools vi får brug for.

## Setup

Du kan vælge at køre det lokalt på din egen linux maskine eller i en docker container som vi på forhånd har bygget. Vi anbefaler den sidste løsning.
Hvis du kører linux beskriver vi under hvordan under, men kører du windows eller mac er du på egen hånd. 
For at kunne deltage aktivt i webinaret er det vigtigt at du på den ene eller anden måde kan køre ropper med vores firmware.
Skulle det ske at du ikke kan få det til at virke så deltag dog gerne aligevel, hvis tiden tilader det kan vi få det til at virker undervejs.

### Docker setup
 
Start med at installere docker på din maskine:
 
Her er en guilde til ubuntu og det burde være nogen lunde det samme på andre distros (google is you frind):
```bash
sudo apt-get update
sudo apt install docker.io
sudo systemctl start docker
```

clone nu vores repo eller hent den som zip fra github:
 ```bash
git clone https://github.com/Lyrebirds/cable-haunt-webinar
cd cable-haunt-webinar
```

Derefter køre disse 3 commands for at bygge og starte docker containeren:
```bash
sudo docker build -t cable-haunt-webinar .
sudo docker run --name cable-haunt-webinar -d --rm -it cable-haunt-webinar
sudo docker exec -it cable-haunt-webinar /bin/bash
```

hvis du nu ser noget ala `root@91aed89ba72d:~# ` burde du være klar til webinaret.

### lokalt setup
Her antager vi at du i forvejen har python3 og pip3 installeret

 `git clone --recurse-submodules -j8  https://github.com/Lyrebirds/cable-haunt-webinar`
 
 der næst installer disse pip pakker:
```bash
RUN pip3 install --upgrade pwntools
RUN pip3 install --upgrade future
RUN pip3 install --upgrade filebytes
```
Kør nu ropper med:
```bash
cd cable-haunt-webinar
./startRopper.sh
```
hvis du får dette output burde alt virke:

```bash
[INFO] Load gadgets for section: bytes
[LOAD] loading... 100%
[LOAD] filtering badbytes... 100%
(TC7230-EB.01.bin/RAW/MIPSBE)>
```
## Ghidra
Med forde kan du også installere ghidra for at berede kunne reverse engineer firmware men det er ikke en nødvendighed.
Der ligger også en ghidra database TC7230-EB.01.gar i projekt mappen som du kan importere i ghidra.
Den inderholde hele firmwaren med funktions navne og nogle få debug symboler.

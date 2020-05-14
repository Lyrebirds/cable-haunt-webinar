# Cable Haunt Webinar

Dette er vores git repository med alt materiale nødvendigt til ida's webinar "Prøv hacking med Lyrebirds".

Dette repo inderholder den modem firmware vi vil bruge under webinaret samt de tools vi får brug for.

## Setup
Hvis du kører linux kan du selv vælge mellem Docker eller lokalt setup som beskrevet under, vi anbefaler dog Docker. Hvis du kører Windows eller Mac bliver du nød til at bruge Docker, som kan downloades her: <https://www.docker.com/products/docker-desktop>.
Målet med understående setup er at folk får installeret værktøjet "ropper" med vores firmware, så i aktivt kan deltage i webinaret.
Skulle det ske at du ikke kan få det til at virke så deltag dog gerne aligevel, hvis tiden tilader det kan vi få det til at virke undervejs.

### Docker setup
 
Start med at installere docker på din maskine. Her er en guilde til ubuntu og det burde være nogenlunde det samme på andre distros (google is you frind):
```bash
sudo apt-get update
sudo apt install docker.io
sudo systemctl start docker
```

Clone nu dette repo eller hent den som zip fra github:
 ```bash
git clone https://github.com/Lyrebirds/cable-haunt-webinar
cd cable-haunt-webinar
```

Kør derefter disse 3 commands for at bygge og starte docker containeren. Hvis du er på Windows eller Mac skal du selvfølgelig undlade "sudo".
```bash
sudo docker build -t cable-haunt-webinar .
sudo docker run --name cable-haunt-webinar -d --rm -it cable-haunt-webinar
sudo docker exec -it cable-haunt-webinar /bin/bash
```

Hvis du nu ser en terminal med noget ala `root@91aed89ba72d:~# ` burde du være klar til webinaret.

### lokalt setup
Her antager vi at du i forvejen har python3 og pip3 installeret

```
git clone --recurse-submodules -j8  https://github.com/Lyrebirds/cable-haunt-webinar
```
 
Installer disse pip pakker:
```bash
pip3 install --upgrade pwntools
pip3 install --upgrade future
pip3 install --upgrade filebytes
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
Med forde kan du også installere Ghidra for bedre at kunne reverse engineer firmware, dette er dog ikke en nødvendighed. Gihidra er gratis og fungerer cross-platform, <https://ghidra-sre.org/>. Efter du har installeret Ghidra kan du importere filen `TC7230-EB.01.gar` i projekt mappen. Dette er den firmware som modemmerne i vil hacke kører, med funktions navne og nogle få debug symboler. Dette vil kunne hjælpe jer med at finde ud af hvilke funktioner vi kommer til at kalde med vores payload og derved hjælpe jer med at debugge jeres payload.

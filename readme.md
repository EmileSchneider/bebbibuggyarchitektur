# Bebbibuggy Architektur
Die Architektur besteht aus den folgenden Layer:
 - Sensors
 - Interpretation
 - Decision
 - Driving
Sensors organisiert die Sensormodule des Autos. Jedes Modul ist nur für einen Sensor zuständig und dafür verantwortlich die Sensordaten auf Anfrage zur Verfügung zu stellen. 

Interpretation implementiert ein Interface für Decision. Dieses Interface stellt "Fragen" dar die Decision stellen kann. Jeder Sensor hat ein eigenes Interpretationsmodul das Helpermethoden anbietet.

Decision ist das Gehirn des Autos. Es ist dafür zuständig, abhängig vom State die richtigen Fragen an Interpretation zu stellen und auf Grund der Antworten die richtigen Fahrbefehle zu geben.

Driving implementiert ein Interface für Decision und abstrahiert die Hardware in brauchbare Methoden.
## Implementierung
### Sensors
Jeder Sensor ist eine Klasse die ein Interface Implementiert.
### Interpretation 
Zu jedem Sensor gibt es ein Analyseobjekt. Jenes bekommt über Dependency Injection seinen jeweiligen Sensor und  bietet Helfermethoden und Teilinterpretationen der Sensordaten per Interface an. 
###### Questions Interface
Das Questionsinterface trennt die Analyse der Sensorendaten von den Fahrentscheidungen. Dabei wird bei der Implementierung von Decision klar werden welche Interpretationen und welche Informationen gebraucht werden. 
Das Questioninterface benutzt die Analyseobjekte um auf jede Anfrage nur die notwendingen Interpretationen der Sensordaten anzufragen.x

### Decision
Decision implementiert eine State Machine um das Auto im Kontext zu steuern. Decision ist auch für die Initialisierung 
des Autos (Sensoren) in einem BOOT State verantwortlich.
## Vorteile 
##### Erweiterbar 
Neue Sensoren können problemlos ergänzt und bestehende in der Implementation geändert werden ohne das Interpretation 
oder Decision davon betroffen wäre.

Decision kann beliebig verändert werden da es nur von seinem State und den Rückgabewerten des Interfaces abhängt. 
##### Testbar
Das Interface von Interpretation ist Testbar, da jeder konkrete Sensorinput eine konkrete Interpretation liefern 
muss die entweder wahr oder falsch ist.

Genauso laesst sich Decision ohne Sensordaten simmulieren zu muessen testen. Auf gegebene Antworten des 
Questionsinterface muss eine korrekte Fahrentscheidung/State Transition geschehen.
##### Performant
Die Implementierung des Questionsinterface, und der jeweilige Aufruf der SensorenAnalyseMethoden nur auf Anfrage hilft uns dabei unnötigen Memory- und Prozessorverbrauch zu vermeiden.
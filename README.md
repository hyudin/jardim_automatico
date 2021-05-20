# jardim_automatico
Projeto de irrigador automático para plantas para projeto da Universiade Presbiteriana Mackenzie

Hardwares utilizados:
- Raspberry Pi 3 Model B
- Sensor de umidade do solo DHT11
- Fonte para Arduino 5v
- Bomba de irrigação 
- Módulo Relé

Softwares Utilizados:
- Python
- Flask
- Visual Studio Code



O sensor de umidade fora ligado no terra, no 3,3v e em uma das entradas do Raspberry Pi. 
O módulo relé foi conectado ao terra, no 5v e em outra entrada, e, é responsável em ligar e desligar a bomba de irrigação.  
O Arduino foi utilizado somente para fornecer energia a bomba de irrigação. 
Para ligar o servidor do Flask é necessário entrar no terminal e executar o arquivo irrigacao_plantas.py, assim os usuários locais conseguem acessar o site através do endereço IP do Raspberry. 
No site, o usuário poderá ativar e desativar a irrigação automática, assim como irrigar, checar a temperatura e umidade da planta e ver qual a última vez que o solo foi irrigado.
As funções foram armazenadas no arquivo water.py, que possui todas as funções dos botões que estão no site. 
O arquivo irrigacao_plantas.py implementa o flask no projeto e permite que o Raspberry seja acessado em seu endereço.
O Raspberry Pi está utilizando uma versão full do sistema operacional padrão do Raspberry Pi OS. 

## Lesson 11. 2022/02/18

#### 
![Django Request & Response cycle](https://i.redd.it/jksj10krs0s31.jpg)
![](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Operating_system_placement.svg/330px-Operating_system_placement.svg.png)
![](https://about.gitlab.com/images/blogimages/containers-vm-bare-metal.png)
1. Bare metal
2. Virtualization
   1. Hypervisor types 
   ![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Hyperviseur.svg/1024px-Hyperviseur.svg.png)
   ![](https://sbercloud.ru/ru/images/pages/warp/tipy-gipervizorov/types.png)
      1. Native (Type 1) - Автономний гіпервізор завантажується початковим завантажувачем або firmware, і запускає у окремих віртуальних машинах сконфігуровані операційні системи. Деякі автономні гіпервізори мають власні драйвери пристроїв і планувальник.
         1. The most common/used
            1. KVM (Native)
            2. Hyper-V (Native/Type1+ Hybrid)
            3. VMware ESXi (Native)
      2. Hosted (Type 2) - Це компонент, який працює в одному кільці з ядром основної ОС («кільце 0», за термінологією архітектури x86). Гостьовий код може виконуватися безпосередньо на фізичному процесорі, але доступ до пристроїв вводу-виводу комп'ютера з гостьової ОС здійснюється через другий компонент, звичайний процес основної ОС — монітор рівня користувача.
         1. The most common/used
            1. Virtual Box 
            2. VMware Workstation 
   2. Additional
      ![](https://qph.fs.quoracdn.net/main-qimg-07df9d992f2afecda4b5f097d94dfa7e.webp)
      1. Виділений сервер (dedicated server, дедик)
      2. Virtual Private Server (VPS, впска) or Virtual Dedicated Server (VDS, вдска)
      3. Hosting
      4. Saas? 
3. Containers(Docker)
   ![](https://lh6.googleusercontent.com/JLzilHI8wTeXfpclTthVU8Tkg4F_pWBbFwf8lsgHycscIAcK8fslXQlW06lb5lYnfEK-eJXHvvSFNbnANY5A4O6js7KY1ic-Y1jvt-UbTB3aHzq7AOrv0CSotz8vpK5K4Xpj0BMH)
   ![](https://lh6.googleusercontent.com/OLNkuRtYmA-8DwJ1-gSM9HL4Uxu56ae3yX5deu9997DXNtNEFbaAnuwSTlKFbAlmwH8GqJohKNow8gpDbUj_LPqW1sfXBu7CLDFB2cL5jqCuuLiOc89AKdH2yiYkq-37EdnePetq)
   ![](https://techso.ca/wp-content/uploads/2020/05/Capture-d%E2%80%99e%CC%81cran-le-2020-05-07-a%CC%80-17.11.23.png)
   ![](https://lh3.googleusercontent.com/guEcIQ8rmHR0S29wqoqv9Vs_Qz5T8JWckynh5Z4_EVfZOLSpUyZ-w_fexPhZlgGC1T6mT0oJZScTky7co6yrDVyvY0gp_gxtOj1omsEyicTkdp9m1DmhGnVLFr1yVsev7AvHG2s)
   2. Docker containers orchestration
      1. Docker compose
      2. Docker swarm
      3. Kubernetes (K8s)
         ![](https://lh3.googleusercontent.com/11JEgdjXgakrp8WuE4ZclwX_4pIlsRr0wrxnoefWzR8ORz_EM-3tfSfbR6kerrNqs_wTkIgTIPTS1Epf-ad_YeEnLO3eGc0kN0kqen4I8eqOGLB0I2w1H414T40iZYhYTTo8x3NK)
         ![](https://rtfm.co.ua/wp-content/uploads/2019/07/07751442-deployment.png)

4. Back to reality. Docker


### Reading
1. https://en.wikipedia.org/wiki/Operating_system
2. https://en.wikipedia.org/wiki/Hypervisor
3. https://uk.wikipedia.org/wiki/%D0%93%D1%96%D0%BF%D0%B5%D1%80%D0%B2%D1%96%D0%B7%D0%BE%D1%80
4. https://sbercloud.ru/ru/warp/tipy-gipervizorov
5. https://habr.com/ru/company/flant/blog/327338/
6. https://soshace.com/dockerizing-django-with-postgres-redis-and-celery/
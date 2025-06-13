
# Stealthveil - IP & MAC Address Management Tool EN

## Description

Stealthveil is a command line tool for changing MAC and IP addresses of network interfaces, backing up old addresses and accessing backups on Linux-based systems. The program makes it easy to manage network interface addresses with user-friendly menus.

**Important:** The program is intended to be used for legal and ethical purposes only, especially in test and educational environments. It should not be used for harmful purposes. No responsibility for user misuse is accepted.

---

## Features

* Change the MAC address of network interfaces manually or randomly
* Change the IP address of network interfaces
* Automatic backup of previous MAC and IP addresses
* Easy access to saved backups
* Possibility to clean backup files
* Works with root authorization

---

## Installation and Operation

1. Open the terminal.
2. Download or create the program file.
3. You need to run it with `sudo`:

   ```bash
   sudo python3 stealthveil.py
   ```

---

## Important Prerequisite

* The program requires **`ifconfig`** to be installed on your system, as it relies on it for network interface management.
* On many modern Linux distributions, `ifconfig` is part of the `net-tools` package, which may not be installed by default.
* To install it, you can run:

  ```bash
  sudo apt install net-tools    # Debian/Ubuntu  
  sudo yum install net-tools    # CentOS/RHEL  
  sudo pacman -S net-tools      # Arch Linux  
  ```

---

## Warning / Disclaimer

This program should only be used for **testing and educational purposes in a secure environment**.

Any malicious, unauthorized or harmful use is prohibited and is the sole responsibility of the user.

The software is provided under the MIT License and the developer cannot be held responsible for misuse.

---

# Stealthveil - IP ve MAC Adresi Yönetim Aracı TR

## Açıklama

Stealthveil, ağ arayüzlerinin MAC ve IP adreslerini değiştirmek, eski adresleri yedeklemek ve Linux tabanlı sistemlerdeki yedeklere erişmek için kullanılan bir komut satırı aracıdır. Program, kullanıcı dostu menülerle ağ arayüz adreslerini yönetmeyi kolaylaştırır.

**Önemli:** Program sadece yasal ve etik amaçlar için, özellikle test ve eğitim ortamlarında kullanılmak üzere tasarlanmıştır. Zararlı amaçlar için kullanılmamalıdır. Kullanıcının yanlış kullanımından dolayı sorumluluk kabul edilmez.

---

## Özellikler

* Ağ arayüzlerinin MAC adresini manuel olarak veya rastgele değiştirin
* Ağ arayüzlerinin IP adresini değiştirme
* Önceki MAC ve IP adreslerinin otomatik yedeklenmesi
* Kayıtlı yedeklere kolay erişim
* Yedekleme dosyalarını temizleme imkanı
* Kök yetkilendirme ile çalışır

---

## Kurulum ve Çalıştırma

1. Terminali açın.
2. Program dosyasını indirin veya oluşturun.
3. Programı `sudo` ile çalıştırmanız gerekir:

   ```bash
   sudo python3 stealthveil.py
   ```

---

## Önemli Önkoşul

* Program, ağ arayüzü yönetimi için **`ifconfig`** aracının kurulu olmasını gerektirir.
* Modern Linux dağıtımlarında `ifconfig` genellikle `net-tools` paketi içinde bulunur ve bazen varsayılan olarak kurulu olmayabilir.
* Kurmak için aşağıdaki komutu kullanabilirsiniz:

  ```bash
  sudo apt install net-tools    # Debian/Ubuntu  
  sudo yum install net-tools    # CentOS/RHEL  
  sudo pacman -S net-tools      # Arch Linux  
  ```

---

## Uyarı / Disclaimer

Bu program yalnızca **test ve eğitim amaçlı, güvenli ortamlarda** kullanılmalıdır.

Kötü niyetli, izinsiz veya zararlı amaçlarla kullanımı yasaktır ve sorumluluk tamamen kullanıcıya aittir.

Yazılım, MIT Lisansı altında sunulmakta olup, geliştirici kötüye kullanımlardan sorumlu tutulamaz.

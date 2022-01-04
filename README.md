

# TLCNKTDL 
## Tiểu Luận Chuyên Ngành KTDL (đại trà)
> Xây dựng dataware house cho hệ thống search engine: quản lý các loại tài liệu: word, pdf, csv, dữ liệu từ SQL server, MySQL, Mongodb, dữ liệu thông tin trang web, dữ liệu hình ảnh trên web, video, dữ liệu mạng xã hội Facebook, ...
## Nhóm
> Trần Hoàng An Bình (18133003) 
> 
> Phạm Văn Hùng(18133018)
## Install
### Cài đặt Cài đặt VMware Workstation Pro 16
 > Cài đặt theo theo link https://athena.edu.vn/huong-dan-cai-dat-phan-mem-ao-hoa-vmware-workstation-16-pro 
 > 
 > lưu ý: bản 16 pro
### Cài đặt Cài đặt Máy ảo ubuntu 20.04 LST
> cài đặt máy ảo theo link https://vinasupport.com/huong-dan-cai-dat-hdh-ubuntu-20-04-lts/
> 
> lưu ý: bản 20.04 LST và Tiếp tực làm với 3 máy
### Cài đặt Java 1.8.0
> sudo apt update
>
> sudo apt install openjdk-8-jdk
### Cài đặt SSH
 #### Cài đặt 
> apt-get install ssh
>
> apt install openssh-server
> 
> reboot
#### Cấu Hình
> vim /etc/ssh/sshd_config
> -	Tìm đoạn # PubkeyAuthentication yes. Bỏ dấu # phía trước thành
> ...
> PubkeyAuthentication yes
> ...
>-	Tìm đoạn PasswordAuthentication no đổi thành
>...
> PasswordAuthentication yes
>..
### Cấu hình host/hostname 
> vim /etc/hosts
> 
>vim /etc/hosts
### Install Hadoop
> dowdload https://archive.apache.org/dist/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz
> 
> Cầu hình theo File hadoop trong Git
### Install HUE
>Cài đặt theo link https://docs.gethue.com/administrator/installation/dependencies/
>
>Edit HUE như Hue.ini
### Install Apache HIVE

>

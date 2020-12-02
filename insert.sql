insert into kategori (deskripsi)
values ("mencuci"),
       ("mandi"),
       ("bbt");

insert into penghuni(namapenghuni)
values ("Mira"),
       ("Ajeng"),
       ("Shofi");

insert into penggunaan(penghuni_id, kategori_id, tanggal_penggunaan)
values (3,2,date('now','localtime'))

select * from penggunaan
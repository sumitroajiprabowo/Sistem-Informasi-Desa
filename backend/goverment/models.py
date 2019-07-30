from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings


class Kelembagaan(models.Model):
    name = models.CharField(_("Nama Kelembagaan"), max_length=50, unique=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "kelembagaan"
        db_table = "pemerintahan_kelembagaan"

    def __str__(self):
        return self.name


class Jabatan(models.Model):
    name = models.CharField(_("Nama_Jabatan"), max_length=50, unique=True)
    kelembagaan = models.ForeignKey(Kelembagaan,
                                    on_delete=models.CASCADE,
                                    related_name='kelambagaan')

    class Meta:
        ordering = ['kelembagaan', 'id']
        verbose_name_plural = "jabatan"
        db_table = "pemerintahan_jabatan"

    def __str__(self):
        return self.name


class Pemerintahan(models.Model):
    # If using ManytoMany
    # kelembagaan = models.ManyToManyField("Kelembagaan",
    #                                      verbose_name=_("nama kelembagaan"),)
    # jabatan = models.ManyToManyField("Jabatan",
    #                                  verbose_name=_("nama jabatan"),)
    kelembagaan = models.ForeignKey("Kelembagaan", verbose_name=_
                                    ("nama kelembagaan"),
                                    on_delete=models.CASCADE)
    jabatan = models.ForeignKey("Jabatan", verbose_name=_("nama jabatan"),
                                on_delete=models.CASCADE)
    name = models.CharField(_("Nama Lengkap"), max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='user_pemdes')

    class Meta:
        # unique_together = ('jabatan', 'user', )
        verbose_name_plural = "Pemerintahan"
        db_table = "pemerintahan_desa"

    def __str__(self):
        return self.name


class Pelatihan(models.Model):
    name = models.CharField(_("Nama Pelatihan"), max_length=150)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "pelatihan"
        db_table = "pemerintahan_pelatihan"

    def __str__(self):
        return self.name


class ProfilePemerintahan(models.Model):
    STATUS_JABATAN_CHOICES = (
        ('Struktural', 'Struktural'),
        ('Pelaksana', 'Pelaksana'),
        ('Definitif', 'Definitif'),
        ('Pejabat', 'Pejabat'),
        ('PLT', 'PLT'),
        ('YMT', 'YMT'),
    )
    GENDER_CHOICES = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    )
    STATUS_CHOICES = (
        ('Belum Kawin', 'Belum Kawin'),
        ('Kawin', 'Kawin'),
        ('Cerai Hidup', 'Cerai Hidup'),
        ('Cerai Mati', 'Cerai Mati'),
    )
    RELIGION_CHOICES = (
        ('Islam', 'Islam'),
        ('Kristen', 'Kristen'),
        ('Katholik', 'Katholik'),
        ('Hindu', 'Hindu'),
        ('Budha', 'Budha'),
        ('Khong Hucu', 'Khong Hucu'),
    )
    JOB_CHOICES = (
        ('Belum/Tidak Bekerja', 'Belum/Tidak Bekerja'),
        ('Mengurus Rumah Tangga', 'Mengurus Rumah Tangga'),
        ('Pelajar/Mahasiswa', 'Pelajar/Mahasiswa'),
        ('Pensiunan', 'Pensiunan'),
        ('Pegawai Negeri Sipil', 'Pegawai Negeri Sipil'),
        ('Tentara Nasional Indonesia', 'Tentara Nasional Indonesia'),
        ('Kepolisian RI', 'Kepolisian RI'),
        ('Perdagangan', 'Perdagangan'),
        ('Petani/Pekebun', 'Petani/Pekebun'),
        ('Peternak', 'Peternak'),
        ('Nelayan/Perikanan', 'Nelayan/Perikanan'),
        ('Industri', 'Industri'),
        ('Konstruksi', 'Konstruksi'),
        ('Transportasi', 'Transportasi'),
        ('Karyawan Swasta', 'Karyawan Swasta'),
        ('Karyawan BUMN', 'Karyawan BUMN'),
        ('Karyawan BUMD', 'Karyawan BUMD'),
        ('Karyawan Honorer', 'Karyawan Honorer'),
        ('Buruh Harian Lepas', 'Buruh Harian Lepas'),
        ('Buruh Tani/Perkebunan', 'Buruh Tani/Perkebunan'),
        ('Buruh Nelayan/Perikanan', 'Buruh Nelayan/Perikanan'),
        ('Buruh Peternakan', 'Buruh Peternakan'),
        ('Pembantu Rumah Tangga', 'Pembantu Rumah Tangga'),
        ('Tukang Cukur', 'Tukang Cukur'),
        ('Tukang Listrik', 'Tukang Listrik'),
        ('Tukang Batu', 'Tukang Batu'),
        ('Tukang Kayu', 'Tukang Kayu'),
        ('Tukang Sol Sepatu', 'Tukang Sol Sepatu'),
        ('Tukang Las/Pandai Besi', 'Tukang Las/Pandai Besi'),
        ('Tukang Jahit', 'Tukang Jahit'),
        ('Penata Rambut', 'Penata Rambut'),
        ('Penata Rias', 'Penata Rias'),
        ('Penata Busana', 'Penata Busana'),
        ('Mekanik', 'Mekanik'),
        ('Tukang Gigi', 'Tukang Gigi'),
        ('Seniman', 'Seniman'),
        ('Tabib', 'Tabib'),
        ('Paraji', 'Paraji'),
        ('Perancang Busana', 'Perancang Busana'),
        ('Penterjemah', 'Penterjemah'),
        ('Imam Masjid', 'Imam Masjid'),
        ('Pendeta', 'Pendeta'),
        ('Pastur', 'Pastur'),
        ('Wartawan', 'Wartawan'),
        ('Ustadz/Mubaligh', 'Ustadz/Mubaligh'),
        ('Juru Masak', 'Juru Masak'),
        ('Promotor Acara', 'Promotor Acara'),
        ('Anggota DPR-RI', 'Anggota DPR-RI'),
        ('Anggota DPD', 'Anggota DPD'),
        ('Anggota BPK', 'Anggota BPK'),
        ('Presiden', 'Presiden'),
        ('Wakil Presiden', 'Wakil Presiden'),
        ('Anggota Mahkamah', 'Anggota Mahkamah'),
        ('Anggota Kabinet/Kementerian', 'Anggota Kabinet/Kementerian'),
        ('Duta Besar', 'Duta Besar'),
        ('Gubernur', 'Gubernur'),
        ('Wakil Gubernur', 'Wakil Gubernur'),
        ('Bupati', 'Bupati'),
        ('Wakil Bupati', 'Wakil Bupati'),
        ('Walikota', 'Walikota'),
        ('Wakil Walikota', 'Wakil Walikota'),
        ('Anggota DPRD Propinsi', 'Anggota DPRD Propinsi'),
        ('Anggota DPRD Kabupaten/Kota', 'Anggota DPRD Kabupaten/Kota'),
        ('Dosen', 'Dosen'),
        ('Guru', 'Guru'),
        ('Pilot', 'Pilot'),
        ('Pengacara', 'Pengacara'),
        ('Notaris', 'Notaris'),
        ('Arsitek', 'Arsitek'),
        ('Akuntan', 'Akuntan'),
        ('Konsultan', 'Konsultan'),
        ('Dokter', 'Dokter'),
        ('Bidan', 'Bidan'),
        ('Perawat', 'Perawat'),
        ('Apoteker', 'Apoteker'),
        ('Psikiater/Psikolog', 'Psikiater/Psikolog'),
        ('Penyiar Televisi', 'Penyiar Televisi'),
        ('Penyiar Radio', 'Penyiar Radio'),
        ('Pelaut', 'Pelaut'),
        ('Peneliti', 'Peneliti'),
        ('Sopir', 'Sopir'),
        ('Pialang', 'Pialang'),
        ('Paranormal', 'Paranormal'),
        ('Pedagang', 'Pedagang'),
        ('Perangkat Desa', 'Perangkat Desa'),
        ('Kepala Desa', 'Kepala Desa'),
        ('Biarawati', 'Biarawati'),
        ('Wiraswasta', 'Wiraswasta'),
        ('Buruh Migran', 'Buruh Migran'),
        ('Lainnya', 'Lainnya')
    )
    PANGKAT_CHOICES = (
        ('Tidak Ada', 'Tidak Ada'),
        ('Juru Muda', 'Juru Muda'),
        ('Juru Muda Tingkat I	', 'Juru Muda Tingkat I	'),
        ('Juru', 'Juru'),
        ('Juru Tingkat I', 'Juru Tingkat I'),
        ('Pengatur Muda', 'Pengatur Muda'),
        ('Pengatur Muda Tingkat I', 'Pengatur Muda Tingkat I'),
        ('Pengatur', 'Pengatur'),
        ('Pengatur Tingkat I', 'Pengatur Tingkat I'),
        ('Penata Muda', 'Penata Muda'),
        ('Penata Muda Tingkat I', 'Penata Muda Tingkat I'),
        ('Penata', 'Penata'),
        ('Penata Tingkat I', 'Penata Tingkat I'),
        ('Pembina', 'Pembina'),
        ('Pembina Tingkat I', 'Pembina Tingkat I'),
        ('Pembina Utama Muda', 'Pembina Utama Muda'),
        ('Pembina UtamaMadya', 'Pembina UtamaMadya'),
        ('Pembina Utama', 'Pembina Utama'),
    )
    GOLONGAN_CHOICES = (
        ('Tidak Ada', 'Tidak Ada'),
        ('I/a', 'I/a'),
        ('I/b', 'I/b'),
        ('I/c', 'I/c'),
        ('I/d', 'I/d'),
        ('II/a', 'II/a'),
        ('II/b', 'II/b'),
        ('II/c', 'II/c'),
        ('II/d', 'II/d'),
        ('III/a', 'III/a'),
        ('III/b', 'III/b'),
        ('III/c', 'III/c'),
        ('III/d', 'III/d'),
        ('IV/a', 'IV/a'),
        ('IV/b', 'IV/b'),
        ('IV/c', 'IV/c'),
        ('IV/d', 'IV/d'),
    )
    EDUCATION_CHOICES = (
        ('Tidak/Belum Sekolah', 'Tidak/Belum Sekolah'),
        ('Tidak Tamat SD/Sederajat', 'Tidak Tamat SD/Sederajat'),
        ('Tamat SD/Sederajat', 'Tamat SD/Sederajat'),
        ('SLTP/Sederajat', 'SLTP/Sederajat'),
        ('SLTA/Sederjat', 'SLTA/Sederjat'),
        ('Diploma I/II', 'Diploma I/II'),
        ('Akademi/Diploma III/S. Muda', 'Akademi/Diploma III/S. Muda'),
        ('DilpomaIV/Strata I', 'DilpomaIV/Strata I'),
        ('Strata II', 'Strata II'),
        ('Strata III', 'Strata III'),
        ('Pendidikan Non Formal', 'Pendidikan Non Formal'),
    )
    pemerintahan = models.OneToOneField("Pemerintahan",
                                        on_delete=models.CASCADE,
                                        related_name='pemdes')
    niap = models.CharField(_("Nomor Induk Aparatur Perangkat"),
                            max_length=50)
    status_jabatan = models.CharField(max_length=10,
                                      choices=STATUS_JABATAN_CHOICES)
    no_sk = models.CharField(_("Nomer SK"), max_length=50, null=True,
                             blank=True)
    tgl_kep_pengangkatan = models.DateField(
        _("Tanggal Keputusan Pengangkatan"),
        auto_now=False, auto_now_add=False, null=True,
        blank=True)
    tgl_pelantikan = models.DateField(_("Tanggal Pelatikan"),
                                      auto_now=False, auto_now_add=False,
                                      null=True, blank=True)
    akhir_masa_jabatan = models.DateField(_("Akhir Masa Jabatan"),
                                          auto_now=False, auto_now_add=False,
                                          null=True, blank=True)
    pekerjaan_asal = models.CharField(max_length=100, choices=JOB_CHOICES,
                                      null=True, blank=True)
    pangkat = models.CharField(max_length=25, choices=PANGKAT_CHOICES,
                               null=True, blank=True)
    golongan = models.CharField(max_length=10, choices=GOLONGAN_CHOICES,
                                null=True, blank=True)
    tmpt_lhr = models.CharField(_("Tempat Lahir"), max_length=50, null=True,
                                blank=True)
    tgl_lhr = models.DateField(_("Tanggal Lahir"),
                               auto_now=False, auto_now_add=False, null=True,
                               blank=True)
    jk = models.CharField(_("Jenis Kelamin"),
                          max_length=1, choices=GENDER_CHOICES, null=True,
                          blank=True)
    agama = models.CharField(max_length=10, choices=RELIGION_CHOICES,
                             null=True, blank=True)
    pendidikan = models.CharField(_("Pendidikan Akhir"),
                                  max_length=50, choices=EDUCATION_CHOICES,
                                  null=True, blank=True)
    siltap = models.DecimalField(_("Penghasilan Tetap"),
                                 max_digits=9, decimal_places=2, null=True,
                                 blank=True)
    tunjangan = models.DecimalField(_("Tunjangan Penghasilan"),
                                    max_digits=9, decimal_places=2, null=True,
                                    blank=True)
    sawah = models.PositiveIntegerField(_("Bengkok Sawah"), null=True,
                                        blank=True)
    darat = models.PositiveIntegerField(_("Bengkok Darat"), null=True,
                                        blank=True)
    alamat = models.CharField(_("Alamat Lengkap"), max_length=150, null=True,
                              blank=True)
    phone = models.CharField(_("Nomor Handphone"), max_length=14, null=True,
                             blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, null=True,
                              blank=True)
    suami_istri = models.CharField(_("Nama Istri/Suami"), max_length=50,
                                   null=True, blank=True)
    tmpt_lhr_suami_istri = models.CharField(_("Tempat Lahir Istri/Suami"),
                                            max_length=50, null=True,
                                            blank=True)
    tgl_lhr_suami_istri = models.DateField(_("Tanggal Lahir Istri/Suami"),
                                           auto_now=False, auto_now_add=False,
                                           null=True, blank=True)
    agama_suami_istri = models.CharField(_("Agama Istri/Suami"),
                                         max_length=10,
                                         choices=RELIGION_CHOICES, null=True,
                                         blank=True)
    pendidikan_suami_istri = models.CharField(_
                                              ("Pendidikan Akhir Istri/Suami"),
                                              max_length=50,
                                              choices=EDUCATION_CHOICES,
                                              null=True, blank=True)
    anak_kandung = models.PositiveIntegerField(_("Total Anak Kandung"),
                                               null=True, blank=True)
    anak_tiri = models.PositiveIntegerField(_("Total Anak Tiri"), null=True,
                                            blank=True)
    anak_angkat = models.PositiveIntegerField(_("Total Anak Angkat"),
                                              null=True, blank=True)
    photo = models.ImageField(_("photo"), null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Profile Pemerintahan"
        db_table = "pemerintahan_profile"

    def __str__(self):
        return self.pemerintahan.name

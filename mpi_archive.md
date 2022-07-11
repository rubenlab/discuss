
# Archive of MPI data

## Where archive files are located

`/usr/users/a/rubsak/share/mpi_data`

## Process of creating archive files

The submition scripts to create archive files can be found in the `/usr/users/rubsak/sw/archive/mpi` folder.

It's core is to use tar's multi-volume command to divide a directory into several 500G archive file storage.

Here is the command for one of the tasks:

`tar -c -L 500G --file=${pool}/pool-ruben-goett/mpi_archive-{0..1000}.tar pool-ruben-goett`

## Validate all archive files

First I checked the output of all submitted tasks and confirmed that all submitted tasks were completed normally.

After that, I submit a read task to read the list of files in all archive files.

Task subbmission files for reading from archives can be found here:

`/usr/users/rubsak/sw/archive/mpi/list_tasks`

Here is the command for reading the archive:

`tar --list -M -f mpi_archive-0.tar -F ${volume_script} --verbose --verbose > index.txt`

The content of volume_script:

```
#! /bin/bash
echo mpi_archive-$(printf "%d" `expr $TAR_VOLUME - 1`).tar >&$TAR_FD
```

## Transfer archive files to archive driver

HPC compute nodes cannot access the archive driver.

So I log in to the HPC transfer node and copy the files to the archive drive through the rsync command.

Here's the command:

`rsync -r -t --size-only /scratch1/projects/rubsak/owner/yi1/archive_mpi/data/ /usr/users/a/rubsak/share/mpi_data`

I use an extra rsync command to ensure all files are copied.

In the case where the two directory files are the same, the rsync command will complete very quick.

## Archive structure

```
mpi_data
├── pool-ruben2-goett
│   ├── 4Goettingen_fromKenny
│   │   ├── mpi_archive-0.tar
│   │   ├── mpi_archive-10.tar
│   │   ├── mpi_archive-11.tar
│   │   ├── mpi_archive-12.tar
│   │   ├── mpi_archive-1.tar
│   │   ├── mpi_archive-2.tar
│   │   ├── mpi_archive-3.tar
│   │   ├── mpi_archive-4.tar
│   │   ├── mpi_archive-5.tar
│   │   ├── mpi_archive-6.tar
│   │   ├── mpi_archive-7.tar
│   │   ├── mpi_archive-8.tar
│   │   └── mpi_archive-9.tar
│   ├── Arsen
│   │   ├── mpi_archive-0.tar
│   │   ├── mpi_archive-1.tar
│   │   ├── mpi_archive-2.tar
│   │   └── mpi_archive-3.tar
│   ├── Lu_UMG
│   │   ├── Lu_scripts
│   │   │   └── mpi_archive-0.tar
│   │   ├── titan
│   │   │   ├── mpi_archive-0.tar
│   │   │   ├── mpi_archive-10.tar
│   │   │   ├── mpi_archive-11.tar
│   │   │   ├── mpi_archive-12.tar
│   │   │   ├── mpi_archive-13.tar
│   │   │   ├── mpi_archive-14.tar
│   │   │   ├── mpi_archive-15.tar
│   │   │   ├── mpi_archive-16.tar
│   │   │   ├── mpi_archive-17.tar
│   │   │   ├── mpi_archive-1.tar
│   │   │   ├── mpi_archive-2.tar
│   │   │   ├── mpi_archive-3.tar
│   │   │   ├── mpi_archive-4.tar
│   │   │   ├── mpi_archive-5.tar
│   │   │   ├── mpi_archive-6.tar
│   │   │   ├── mpi_archive-7.tar
│   │   │   ├── mpi_archive-8.tar
│   │   │   └── mpi_archive-9.tar
│   │   ├── titan_2
│   │   │   ├── mpi_archive-0.tar
│   │   │   ├── mpi_archive-10.tar
│   │   │   ├── mpi_archive-11.tar
│   │   │   ├── mpi_archive-12.tar
│   │   │   ├── mpi_archive-13.tar
│   │   │   ├── mpi_archive-14.tar
│   │   │   ├── mpi_archive-15.tar
│   │   │   ├── mpi_archive-16.tar
│   │   │   ├── mpi_archive-17.tar
│   │   │   ├── mpi_archive-18.tar
│   │   │   ├── mpi_archive-19.tar
│   │   │   ├── mpi_archive-1.tar
│   │   │   ├── mpi_archive-20.tar
│   │   │   ├── mpi_archive-21.tar
│   │   │   ├── mpi_archive-22.tar
│   │   │   ├── mpi_archive-23.tar
│   │   │   ├── mpi_archive-24.tar
│   │   │   ├── mpi_archive-25.tar
│   │   │   ├── mpi_archive-26.tar
│   │   │   ├── mpi_archive-27.tar
│   │   │   ├── mpi_archive-28.tar
│   │   │   ├── mpi_archive-29.tar
│   │   │   ├── mpi_archive-2.tar
│   │   │   ├── mpi_archive-30.tar
│   │   │   ├── mpi_archive-31.tar
│   │   │   ├── mpi_archive-32.tar
│   │   │   ├── mpi_archive-33.tar
│   │   │   ├── mpi_archive-34.tar
│   │   │   ├── mpi_archive-35.tar
│   │   │   ├── mpi_archive-36.tar
│   │   │   ├── mpi_archive-37.tar
│   │   │   ├── mpi_archive-38.tar
│   │   │   ├── mpi_archive-39.tar
│   │   │   ├── mpi_archive-3.tar
│   │   │   ├── mpi_archive-40.tar
│   │   │   ├── mpi_archive-41.tar
│   │   │   ├── mpi_archive-42.tar
│   │   │   ├── mpi_archive-43.tar
│   │   │   ├── mpi_archive-44.tar
│   │   │   ├── mpi_archive-45.tar
│   │   │   ├── mpi_archive-46.tar
│   │   │   ├── mpi_archive-47.tar
│   │   │   ├── mpi_archive-48.tar
│   │   │   ├── mpi_archive-49.tar
│   │   │   ├── mpi_archive-4.tar
│   │   │   ├── mpi_archive-50.tar
│   │   │   ├── mpi_archive-51.tar
│   │   │   ├── mpi_archive-52.tar
│   │   │   ├── mpi_archive-53.tar
│   │   │   ├── mpi_archive-54.tar
│   │   │   ├── mpi_archive-55.tar
│   │   │   ├── mpi_archive-56.tar
│   │   │   ├── mpi_archive-57.tar
│   │   │   ├── mpi_archive-58.tar
│   │   │   ├── mpi_archive-59.tar
│   │   │   ├── mpi_archive-5.tar
│   │   │   ├── mpi_archive-6.tar
│   │   │   ├── mpi_archive-7.tar
│   │   │   ├── mpi_archive-8.tar
│   │   │   └── mpi_archive-9.tar
│   │   └── titan_to_Lu
│   │       ├── mpi_archive-0.tar
│   │       ├── mpi_archive-10.tar
│   │       ├── mpi_archive-11.tar
│   │       ├── mpi_archive-12.tar
│   │       ├── mpi_archive-13.tar
│   │       ├── mpi_archive-14.tar
│   │       ├── mpi_archive-15.tar
│   │       ├── mpi_archive-16.tar
│   │       ├── mpi_archive-17.tar
│   │       ├── mpi_archive-18.tar
│   │       ├── mpi_archive-19.tar
│   │       ├── mpi_archive-1.tar
│   │       ├── mpi_archive-20.tar
│   │       ├── mpi_archive-21.tar
│   │       ├── mpi_archive-22.tar
│   │       ├── mpi_archive-23.tar
│   │       ├── mpi_archive-24.tar
│   │       ├── mpi_archive-25.tar
│   │       ├── mpi_archive-26.tar
│   │       ├── mpi_archive-27.tar
│   │       ├── mpi_archive-28.tar
│   │       ├── mpi_archive-29.tar
│   │       ├── mpi_archive-2.tar
│   │       ├── mpi_archive-30.tar
│   │       ├── mpi_archive-31.tar
│   │       ├── mpi_archive-32.tar
│   │       ├── mpi_archive-33.tar
│   │       ├── mpi_archive-34.tar
│   │       ├── mpi_archive-35.tar
│   │       ├── mpi_archive-36.tar
│   │       ├── mpi_archive-37.tar
│   │       ├── mpi_archive-38.tar
│   │       ├── mpi_archive-39.tar
│   │       ├── mpi_archive-3.tar
│   │       ├── mpi_archive-40.tar
│   │       ├── mpi_archive-41.tar
│   │       ├── mpi_archive-42.tar
│   │       ├── mpi_archive-43.tar
│   │       ├── mpi_archive-44.tar
│   │       ├── mpi_archive-45.tar
│   │       ├── mpi_archive-46.tar
│   │       ├── mpi_archive-4.tar
│   │       ├── mpi_archive-5.tar
│   │       ├── mpi_archive-6.tar
│   │       ├── mpi_archive-7.tar
│   │       ├── mpi_archive-8.tar
│   │       └── mpi_archive-9.tar
│   ├── Patricia
│   │   ├── mpi_archive-0.tar
│   │   └── mpi_archive-1.tar
│   ├── pool-ruben2-ls-alRt_17022022.txt
│   └── Tat
│       └── mpi_archive-0.tar
├── pool-ruben-goett
│   ├── mpi_archive-0.tar
│   ├── mpi_archive-10.tar
│   ├── mpi_archive-11.tar
│   ├── mpi_archive-12.tar
│   ├── mpi_archive-13.tar
│   ├── mpi_archive-14.tar
│   ├── mpi_archive-15.tar
│   ├── mpi_archive-16.tar
│   ├── mpi_archive-17.tar
│   ├── mpi_archive-18.tar
│   ├── mpi_archive-19.tar
│   ├── mpi_archive-1.tar
│   ├── mpi_archive-20.tar
│   ├── mpi_archive-21.tar
│   ├── mpi_archive-22.tar
│   ├── mpi_archive-23.tar
│   ├── mpi_archive-24.tar
│   ├── mpi_archive-25.tar
│   ├── mpi_archive-2.tar
│   ├── mpi_archive-3.tar
│   ├── mpi_archive-4.tar
│   ├── mpi_archive-5.tar
│   ├── mpi_archive-6.tar
│   ├── mpi_archive-7.tar
│   ├── mpi_archive-8.tar
│   └── mpi_archive-9.tar
├── pool-sakata2-goett
│   ├── 26S_Rpn1_Paper
│   │   └── mpi_archive-0.tar
│   ├── AS
│   │   ├── mpi_archive-0.tar
│   │   ├── mpi_archive-1.tar
│   │   ├── mpi_archive-2.tar
│   │   ├── mpi_archive-3.tar
│   │   ├── mpi_archive-4.tar
│   │   ├── mpi_archive-5.tar
│   │   ├── mpi_archive-6.tar
│   │   ├── mpi_archive-7.tar
│   │   ├── mpi_archive-8.tar
│   │   └── mpi_archive-9.tar
│   ├── Eri
│   │   └── mpi_archive-0.tar
│   ├── Finley_paper
│   │   └── mpi_archive-0.tar
│   ├── Marc
│   │   ├── mpi_archive-0.tar
│   │   ├── mpi_archive-1.tar
│   │   └── mpi_archive-2.tar
│   ├── Markus
│   │   ├── mpi_archive-0.tar
│   │   └── SPA
│   │       ├── T1K2
│   │       │   ├── mpi_archive-0.tar
│   │       │   ├── mpi_archive-10.tar
│   │       │   ├── mpi_archive-11.tar
│   │       │   ├── mpi_archive-12.tar
│   │       │   ├── mpi_archive-13.tar
│   │       │   ├── mpi_archive-14.tar
│   │       │   ├── mpi_archive-15.tar
│   │       │   ├── mpi_archive-16.tar
│   │       │   ├── mpi_archive-17.tar
│   │       │   ├── mpi_archive-18.tar
│   │       │   ├── mpi_archive-19.tar
│   │       │   ├── mpi_archive-1.tar
│   │       │   ├── mpi_archive-20.tar
│   │       │   ├── mpi_archive-21.tar
│   │       │   ├── mpi_archive-22.tar
│   │       │   ├── mpi_archive-23.tar
│   │       │   ├── mpi_archive-24.tar
│   │       │   ├── mpi_archive-25.tar
│   │       │   ├── mpi_archive-26.tar
│   │       │   ├── mpi_archive-27.tar
│   │       │   ├── mpi_archive-28.tar
│   │       │   ├── mpi_archive-29.tar
│   │       │   ├── mpi_archive-2.tar
│   │       │   ├── mpi_archive-30.tar
│   │       │   ├── mpi_archive-31.tar
│   │       │   ├── mpi_archive-32.tar
│   │       │   ├── mpi_archive-33.tar
│   │       │   ├── mpi_archive-34.tar
│   │       │   ├── mpi_archive-35.tar
│   │       │   ├── mpi_archive-36.tar
│   │       │   ├── mpi_archive-37.tar
│   │       │   ├── mpi_archive-38.tar
│   │       │   ├── mpi_archive-39.tar
│   │       │   ├── mpi_archive-3.tar
│   │       │   ├── mpi_archive-40.tar
│   │       │   ├── mpi_archive-41.tar
│   │       │   ├── mpi_archive-42.tar
│   │       │   ├── mpi_archive-43.tar
│   │       │   ├── mpi_archive-44.tar
│   │       │   ├── mpi_archive-45.tar
│   │       │   ├── mpi_archive-46.tar
│   │       │   ├── mpi_archive-47.tar
│   │       │   ├── mpi_archive-48.tar
│   │       │   ├── mpi_archive-49.tar
│   │       │   ├── mpi_archive-4.tar
│   │       │   ├── mpi_archive-50.tar
│   │       │   ├── mpi_archive-51.tar
│   │       │   ├── mpi_archive-52.tar
│   │       │   ├── mpi_archive-53.tar
│   │       │   ├── mpi_archive-54.tar
│   │       │   ├── mpi_archive-55.tar
│   │       │   ├── mpi_archive-56.tar
│   │       │   ├── mpi_archive-57.tar
│   │       │   ├── mpi_archive-58.tar
│   │       │   ├── mpi_archive-59.tar
│   │       │   ├── mpi_archive-5.tar
│   │       │   ├── mpi_archive-60.tar
│   │       │   ├── mpi_archive-61.tar
│   │       │   ├── mpi_archive-62.tar
│   │       │   ├── mpi_archive-63.tar
│   │       │   ├── mpi_archive-64.tar
│   │       │   ├── mpi_archive-65.tar
│   │       │   ├── mpi_archive-66.tar
│   │       │   ├── mpi_archive-67.tar
│   │       │   ├── mpi_archive-68.tar
│   │       │   ├── mpi_archive-69.tar
│   │       │   ├── mpi_archive-6.tar
│   │       │   ├── mpi_archive-70.tar
│   │       │   ├── mpi_archive-71.tar
│   │       │   ├── mpi_archive-72.tar
│   │       │   ├── mpi_archive-73.tar
│   │       │   ├── mpi_archive-74.tar
│   │       │   ├── mpi_archive-75.tar
│   │       │   ├── mpi_archive-76.tar
│   │       │   ├── mpi_archive-77.tar
│   │       │   ├── mpi_archive-78.tar
│   │       │   ├── mpi_archive-79.tar
│   │       │   ├── mpi_archive-7.tar
│   │       │   ├── mpi_archive-80.tar
│   │       │   ├── mpi_archive-81.tar
│   │       │   ├── mpi_archive-82.tar
│   │       │   ├── mpi_archive-83.tar
│   │       │   ├── mpi_archive-84.tar
│   │       │   ├── mpi_archive-85.tar
│   │       │   ├── mpi_archive-86.tar
│   │       │   ├── mpi_archive-8.tar
│   │       │   └── mpi_archive-9.tar
│   │       └── T1K3
│   │           ├── mpi_archive-0.tar
│   │           ├── mpi_archive-10.tar
│   │           ├── mpi_archive-11.tar
│   │           ├── mpi_archive-12.tar
│   │           ├── mpi_archive-13.tar
│   │           ├── mpi_archive-14.tar
│   │           ├── mpi_archive-15.tar
│   │           ├── mpi_archive-16.tar
│   │           ├── mpi_archive-17.tar
│   │           ├── mpi_archive-18.tar
│   │           ├── mpi_archive-19.tar
│   │           ├── mpi_archive-1.tar
│   │           ├── mpi_archive-20.tar
│   │           ├── mpi_archive-21.tar
│   │           ├── mpi_archive-22.tar
│   │           ├── mpi_archive-23.tar
│   │           ├── mpi_archive-2.tar
│   │           ├── mpi_archive-3.tar
│   │           ├── mpi_archive-4.tar
│   │           ├── mpi_archive-5.tar
│   │           ├── mpi_archive-6.tar
│   │           ├── mpi_archive-7.tar
│   │           ├── mpi_archive-8.tar
│   │           └── mpi_archive-9.tar
│   ├── Rpn1_Folder
│   │   └── mpi_archive-0.tar
│   ├── Tat
│   │   ├── mpi_archive-0.tar
│   │   ├── mpi_archive-1.tar
│   │   ├── mpi_archive-2.tar
│   │   ├── mpi_archive-3.tar
│   │   ├── mpi_archive-4.tar
│   │   ├── mpi_archive-5.tar
│   │   └── mpi_archive-6.tar
│   ├── Till
│   │   ├── mpi_archive-0.tar
│   │   └── mpi_archive-1.tar
│   └── Ubp6
│       └── mpi_archive-0.tar
├── pool-sakata-goett
│   ├── AS
│   │   ├── mpi_archive-0.tar
│   │   ├── mpi_archive-10.tar
│   │   ├── mpi_archive-11.tar
│   │   ├── mpi_archive-12.tar
│   │   ├── mpi_archive-13.tar
│   │   ├── mpi_archive-14.tar
│   │   ├── mpi_archive-15.tar
│   │   ├── mpi_archive-16.tar
│   │   ├── mpi_archive-17.tar
│   │   ├── mpi_archive-18.tar
│   │   ├── mpi_archive-19.tar
│   │   ├── mpi_archive-1.tar
│   │   ├── mpi_archive-20.tar
│   │   ├── mpi_archive-21.tar
│   │   ├── mpi_archive-22.tar
│   │   ├── mpi_archive-23.tar
│   │   ├── mpi_archive-24.tar
│   │   ├── mpi_archive-25.tar
│   │   ├── mpi_archive-26.tar
│   │   ├── mpi_archive-27.tar
│   │   ├── mpi_archive-28.tar
│   │   ├── mpi_archive-29.tar
│   │   ├── mpi_archive-2.tar
│   │   ├── mpi_archive-30.tar
│   │   ├── mpi_archive-31.tar
│   │   ├── mpi_archive-32.tar
│   │   ├── mpi_archive-33.tar
│   │   ├── mpi_archive-34.tar
│   │   ├── mpi_archive-35.tar
│   │   ├── mpi_archive-36.tar
│   │   ├── mpi_archive-37.tar
│   │   ├── mpi_archive-38.tar
│   │   ├── mpi_archive-39.tar
│   │   ├── mpi_archive-3.tar
│   │   ├── mpi_archive-40.tar
│   │   ├── mpi_archive-41.tar
│   │   ├── mpi_archive-42.tar
│   │   ├── mpi_archive-43.tar
│   │   ├── mpi_archive-44.tar
│   │   ├── mpi_archive-45.tar
│   │   ├── mpi_archive-46.tar
│   │   ├── mpi_archive-4.tar
│   │   ├── mpi_archive-5.tar
│   │   ├── mpi_archive-6.tar
│   │   ├── mpi_archive-7.tar
│   │   ├── mpi_archive-8.tar
│   │   └── mpi_archive-9.tar
│   ├── Eri
│   │   ├── mpi_archive-0.tar
│   │   ├── mpi_archive-1.tar
│   │   └── mpi_archive-2.tar
│   ├── Marc
│   │   ├── mpi_archive-0.tar
│   │   └── mpi_archive-1.tar
│   ├── Markus
│   │   ├── mpi_archive-0.tar
│   │   ├── mpi_archive-1.tar
│   │   ├── mpi_archive-2.tar
│   │   ├── mpi_archive-3.tar
│   │   ├── mpi_archive-4.tar
│   │   └── mpi_archive-5.tar
│   ├── Nikki
│   │   └── mpi_archive-0.tar
│   ├── other
│   │   └── mpi_archive-0.tar
│   ├── Students
│   │   └── mpi_archive-0.tar
│   └── Tat
│       ├── mpi_archive-0.tar
│       ├── mpi_archive-10.tar
│       ├── mpi_archive-1.tar
│       ├── mpi_archive-2.tar
│       ├── mpi_archive-3.tar
│       ├── mpi_archive-4.tar
│       ├── mpi_archive-5.tar
│       ├── mpi_archive-6.tar
│       ├── mpi_archive-7.tar
│       ├── mpi_archive-8.tar
│       └── mpi_archive-9.tar
└── pool-titan6-goett
    ├── AS
    │   ├── mpi_archive-0.tar
    │   ├── mpi_archive-10.tar
    │   ├── mpi_archive-11.tar
    │   ├── mpi_archive-12.tar
    │   ├── mpi_archive-13.tar
    │   ├── mpi_archive-14.tar
    │   ├── mpi_archive-15.tar
    │   ├── mpi_archive-1.tar
    │   ├── mpi_archive-2.tar
    │   ├── mpi_archive-3.tar
    │   ├── mpi_archive-4.tar
    │   ├── mpi_archive-5.tar
    │   ├── mpi_archive-6.tar
    │   ├── mpi_archive-7.tar
    │   ├── mpi_archive-8.tar
    │   └── mpi_archive-9.tar
    └── Tat
        ├── mpi_archive-0.tar
        ├── mpi_archive-10.tar
        ├── mpi_archive-11.tar
        ├── mpi_archive-12.tar
        ├── mpi_archive-13.tar
        ├── mpi_archive-14.tar
        ├── mpi_archive-15.tar
        ├── mpi_archive-16.tar
        ├── mpi_archive-17.tar
        ├── mpi_archive-18.tar
        ├── mpi_archive-19.tar
        ├── mpi_archive-1.tar
        ├── mpi_archive-20.tar
        ├── mpi_archive-21.tar
        ├── mpi_archive-22.tar
        ├── mpi_archive-23.tar
        ├── mpi_archive-24.tar
        ├── mpi_archive-25.tar
        ├── mpi_archive-26.tar
        ├── mpi_archive-27.tar
        ├── mpi_archive-28.tar
        ├── mpi_archive-29.tar
        ├── mpi_archive-2.tar
        ├── mpi_archive-30.tar
        ├── mpi_archive-31.tar
        ├── mpi_archive-32.tar
        ├── mpi_archive-33.tar
        ├── mpi_archive-34.tar
        ├── mpi_archive-35.tar
        ├── mpi_archive-36.tar
        ├── mpi_archive-37.tar
        ├── mpi_archive-38.tar
        ├── mpi_archive-39.tar
        ├── mpi_archive-3.tar
        ├── mpi_archive-40.tar
        ├── mpi_archive-41.tar
        ├── mpi_archive-42.tar
        ├── mpi_archive-43.tar
        ├── mpi_archive-44.tar
        ├── mpi_archive-45.tar
        ├── mpi_archive-46.tar
        ├── mpi_archive-47.tar
        ├── mpi_archive-48.tar
        ├── mpi_archive-4.tar
        ├── mpi_archive-5.tar
        ├── mpi_archive-6.tar
        ├── mpi_archive-7.tar
        ├── mpi_archive-8.tar
        └── mpi_archive-9.tar
```
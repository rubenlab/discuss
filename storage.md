# Storage Document

## Abstract

This document describes how to store and transmit the experimental data of each stage.
## Background

Our various experimental equipment produces large amounts of data every day, especially the EM.

Storage devices directly connected to our equipments(instrument PCs) are small in capacity, have no backup, and cannot be accessed remotely. Experimental data needs to be transferred to other mass storage devices as soon as possible.

At the same time, the storage devices should be able accessible to the data processing devices, and need to ensure sufficient read and write speed to support the data processing programs.

Another important factor is that the storage device needs to avoid accidental data loss as much as possible.

### Data processing nodes

We currently have two data processing nodes:

- The pre-processing server at Physics
- The HPC

### Data storage devices

We have three storage devices of sufficient capacity:

- Our storage server with 300TB storage space.
- The scratch folder on the HPC with 1.3PB storage space shared with other groups.
- The archive storage on the HPC

#### Storage Server

The storage server uses a raid6 disk array, and two of the 28 disks are allowed to be damaged without data loss.

It is on the same network segment with the pre-processing server, and the pre-processing program can access the data on the storage server at a fast speed.

#### HPC scratch storage

The data on the HPC scratch is stored on the SSD raid disk array, and there is no data backup.

Data on scratch driver can be accessed by data processing programs on the HPC.

#### HPC archive storage

The archive storage space has nearly unlimited capacity and is automatically backed up in two different places.

It is slow to read and not suitable for data processing.

It is not suitable for storing a large number of small files. Deleting files does not free up space on the archive drive.

### Data

Data can be divided into three types:

- Original data, it's produced directly by the equipments.
- Intermediate data, which can be obtained by processing the original data through a series of processing procedures.
- Final result, it's the final processed intermediate data.

## Proposal

Data processing and migration process:

EM->Falcon4 server->Pre-processing->HPC


### Pre-processing

Data will be processed on the pre-processing server before moving to HPC.

### Move to HPC

Manually move the pre-processed folder to the "tohpc" folder.

Here's the document:

https://github.com/rubenlab/tohpc

### Archiving on the HPC

On HPC, active data needs to be backed up because there is no automatic data backup on /scratch driver. At the same time, long-term inactive data need to be automatically archived.

The folder structure needs to be normalized to determine which directories need to be automatically backed up and archived.
#### Folder structure

Data should be stored under /scratch1/projects/rubsak/owner/$USER folder, which can be stored in a one-level or two-level folder structure.

One-level folder structure:

```
$USER
├── dataset
              └── frames
```

Two-level folder structure:
```
$USER
├── project
              └── dataset
                           └── frames
```

Two-level structure is more ideal, but considering that the one-level structure is a commonly used structure at present, we support both structures. The location of the "frames" folder determines whether it is a one-level structure or a two-level structure.

#### Back up of hot data

When each new dataset folder is first moved to the HPC, a tar backup on the archive drive will be created for it. We do not make backups for subsequent changes, as these changes can be restored from the original data.

#### Automatic archiving of non-alive data

When all files in one dataset folder have not been modified for a certain period of time (for example, 90 days), this folder will be automatically archived.

<!-- ## Rationale -->

## Implementation

### Move to HPC

Already implimented.

Here's the document:

https://github.com/rubenlab/tohpc

### Archiving on the HPC

#### Folder structure

The correct folder structure needs to be manually maintained.

#### Back up of hot data

The /scratch1/projects/rubsak/owner folder should be scanned by a cron task to create a backup of the newly created and fully transferred dataset folder.

##### Check if it is a new dataset folder

If no corresponding backup file is found, it is considered to be a new dataset folder.

##### Check if it is fully transfered

If there are no newly created files in the folder within 12 hours, the folder is considered to have been fully transferred.

#### Automatic archiving of non-alive data

The /scratch1/projects/rubsak/owner folder is scanned through a cron script, it looks for dataset folders that have not been modified for 90 days and archive them.

## Open issues

### sudo permission

We don't have sudo permission, so all cron scripts need HPC administrators to help us run.
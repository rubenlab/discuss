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




## Rationale

## Implementation

## Open issues
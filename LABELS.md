# header

The section contains general information about the format version and about the body that publishes the result.

## reportStatus [values]

The field can take one of the following values:
- draft
- final
- corrective

## publisher

### confidentialityLevel [values]

The field can take one of the following values:
- public
- internal
- confidential
- secret

### publicKey

The field should contain a public key associated to the algorithm in the contentHash object, which permits to check the traceability of the publication.

## dataTypes

The section describes the profile of data used in the task, if any.

### tabular

#### fileType [values]

The field can take one of the following values:
- csv
- text
- html
- pdf
- ods
- xls
- xlsx

#### volumeUnit [values]

The field can take one of the following values:
- kilobyte
- megabyte
- gigabyte
- terabyte
- petabyte
- exabyte

#### sourceUri [values]

The field can take one of the following values:
- public
- private

#### itemsDimension [properties]

The object's properties should be integer numbers in string format: "1", "2", "3", etc.

### audio

#### fileType [values]

The field can take one of the following values:
- 3gp
- 8svx
- aa
- aac
- aax
- act
- aiff
- alac
- amr
- ape
- au
- awb
- cda
- dss
- dvf
- flac
- gsm
- iklax
- ivs
- m4a
- m4b
- m4p
- mmf
- movpkg
- mp3
- mpc
- msv
- nmf
- ogg
- opus
- ra
- raw
- rf64
- sln
- tta
- voc
- vox
- wav
- wma
- wv
- webm

#### volumeUnit [values]

The field can take one of the following values:
- kilobyte
- megabyte
- gigabyte
- terabyte
- petabyte
- exabyte

#### sourceUri [values]

The field can take one of the following values:
- public
- private

#### itemsDimension [properties]

The object's properties should be integer numbers in string format: "1", "2", "3", etc.

### image

#### fileType [values]

The field can take one of the following values:
- afdesign
- afphoto
- ai
- avif
- bmp
- bpg
- cd5
- cdr
- cgm
- clip
- cpt
- deep
- drawingml
- drw
- ecw
- eps
- fits
- flif
- gem
- gerber
- gif
- gle
- heif
- hp-gl
- hvif
- ico
- ilbm
- img
- img
- jpeg
- kra
- lottie
- mathml
- mdp
- naplps
- netpbm
- nrrd
- odg
- pam
- pbm
- pcx
- pdf
- pdn
- pgf
- pgm
- pgml
- pict
- plbm
- png
- pnm
- postscript
- ppm
- psd
- psp
- pstricks
- qcc
- regis
- sai
- sgi
- sid
- svg
- swf
- tga
- tiff
- tinyvg
- vicar
- vml
- webp
- wmf
- xaml
- xar
- xcf
- xisf
- xps

#### volumeUnit [values]

The field can take one of the following values:
- kilobyte
- megabyte
- gigabyte
- terabyte
- petabyte
- exabyte

#### sourceUri [values]

The field can take one of the following values:
- public
- private

#### itemsDimension [properties]

The object's properties should be integer numbers in string format: "1", "2", "3", etc.

### video

#### fileType [values]

The field can take one of the following values:
- 3gpp
- 3gpp2
- amv
- asf
- avi
- dirac
- divx
- flv
- flvf4v
- gif
- m4v
- matroska
- mpeg1
- mpeg2
- mpeg4
- mxf
- nsv
- ogg
- quicktime
- raw
- realmedia
- roq
- svi
- vivoactive
- vob
- webm
- wmv

#### volumeUnit [values]

The field can take one of the following values:
- kilobyte
- megabyte
- gigabyte
- terabyte
- petabyte
- exabyte

#### sourceUri [values]

The field can take one of the following values:
- public
- private

#### itemsDimension [properties]

The object's properties should be integer numbers in string format: "1", "2", "3", etc.

### object

This is a general 'media' entity, different from all media listed above.

#### volumeUnit [values]

The field can take one of the following values:
- kilobyte
- megabyte
- gigabyte
- terabyte
- petabyte
- exabyte

#### sourceUri [values]

The field can take one of the following values:
- public
- private

#### itemsDimension [properties]

The object's properties should be integer numbers in string format: "1", "2", "3", etc.

# measurementMethod

## software

### CodeCarbon

#### measureUnit

The field can take one of the following values:
- Wh
- kWh
- mWh

### CarbonAI

#### measureUnit

The field can take one of the following values:
- Wh
- kWh
- mWh

### CarbonAI

#### PyJoule

The field can take one of the following values:
- Wh
- kWh
- mWh

## hardware [properties]

The object's properties should be one value among the following:
- Fluke-117
- Fluke-179
- Fluke-87V
- Fluke-87V-MAX
- Fluke-279-FC
- Fluke-179
- Fluke-117
- Fluke-115
- Fluke-177
- Fluke-289
- Fluke-28-II
- Fluke-116
- Fluke-287
- Fluke-3000
- Fluke-114
- Fluke-113
- Fluke-233
- Fluke-83V
- Fluke-28-II
- Fluke-175
- Fluke-27-II
- Fluke-88V
- Fluke-77-IV
- Fluke-v3001-FC
- Fluke-v3000-FC
- Fluke-v3001-FC
- Fluke-107
- Fluke-1587-FC
- Fluke-PRV240
- Fluke-PRV240FS
- Fluke-8808A

			"PCE-PA6000": {
				"instrumentFamily": "WattMeter",
				"instrumentManufacturer": "PCE Instruments",
				"eanCode": "4250348701152",
				"measureUnit": "Wh",
				"measureValue": null		
			}
		}
	},
	"taskContext": {
		"taskDomain": "machine-learning|general-software|gaming|...",
		"taskSubDomain": "deep-learning|reinforcement-learning|...",
		"taskType": "preprocessing|clustering|classification|reinforcement|finetuning|inference",
		"taskSubType": "vectorization",
		"algorithms": {
			"ResNet50": {
				"framework": "TensorFlow",
				"frameworkVersion": "2.14.0",
				"classPath": "tf.keras.applications.resnet50.ResNet50",
				"hyperparameters": {
					"key1": "value1"
				},
				"trainPercent": 0.7,
				"validationPercent": 0.3,
				"testPercent": 0.0
			}
		}
	},
	"systemContext": {
		"os": "Linux",
		"distribution": "RedHat",
		"distributionVersion": "Enterprise Linux 9",
		"kernelVersion": null
	},
	"softwareContext": {
		"language": "python",
		"version": "3.11.6"
	},
	"hardwareContext": {
		"shared": true,
		"cpu": {
			"items": 1,
			"manufacturer": "AMD",
			"family": "Ryzen",
			"series": "7000X3D",
			"share": 0.2
		},
		"gpu": {
			"items": 4,
			"manufacturer": "NVIDIA",
			"family": "GeForce",
			"series": "RTX 4090",
			"share": 0.5
		},
		"motherboard": null,
		"drive": null,
		"fans": null,
		"extra": null
	},
	"environment": {
		"country": "France",
		"latitude": null,
		"longitude": null,
		"location": null,
		"powerSupplierType": "public|private|internal",
		"powerSource": "default|solar|wind|nuclear|hydro|gas|coal|other",
		"powerSourceCarbonIntensityUnit": "gCO2eq/kWh",
		"powerSourceCarbonIntensity": 85
	},
	"contentHash": {
		"algorithm": "RSA",
		"value": "7BBAD02FC4C657A2CC858CD4EA2EC751"
	}
}

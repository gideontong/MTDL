# MembershipToolkit.com Downloader

This is a tool that converts MembershipToolkit.com directories to a parsable CSV. Python 3 is required.

## Getting Started

Run the following in Python 3:

```bash
python setup.py
```

It should then install. Then run:

```bash
membership-toolkit-downloader [URL]
```

with the direct URL to the Membership Toolkit subdomain you want to point at. The script will automatically convert all members into a parseable CSV.

Use the flag `--json` to get a JSON output instead.

## Motivation

My high school's PTSA uses this system and wants us to pay for access to the directory, and I don't want to pay. So I wrote this instead to dump the addresses.

## Contact

If you have questions, please contact [Gideon Tong](mailto:gideontong@gideontong.com).

## License

MIT License (c) 2019-2020 Gideon Tong

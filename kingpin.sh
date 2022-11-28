#!/bin/sh

pin="-";
new_pin="";
while [ "${pin}" != "${new_pin}" ]; do
	pin="${new_pin}";
	max_calls=0;
	for i in $(seq -1 9); do
		sleep_count=$(echo "${new_pin}${i}" | ltrace ./kingpin |& grep -c usleep);
		if [ "${max_calls}" -lt "${sleep_count}" ]; then
			if [ "${i}" -gt -1 ]; then
				new_pin="${pin}${i}";
				echo "${new_pin}";
				break;
			fi
			max_calls="${sleep_count}";
		fi
	done
done

echo;
echo "pin is ${pin}";

echo "${pin}" | ./kingpin
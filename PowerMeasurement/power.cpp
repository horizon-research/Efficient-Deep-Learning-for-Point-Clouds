#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/fcntl.h>
#include <time.h>

#include <string>
#include <vector>
#include <map>
#include <thread>

using namespace std;

map <string, string> pc_map;

void power_consumption_loop(int fd, FILE *fp);

void single_power_loop(const string &mode, const string &title);

int Open(const char *s, int mode);

/**
 * Dump average power consumption value to stderr
 */
void power_consumption_loop(int fd, FILE *fp) {
 	int cnt = 0;
 	double sum = 0;
 	double start = 0;

 	while (true) {
  		if (cnt == 0) {
  			struct timespec tv;
  			clock_gettime(CLOCK_MONOTONIC_RAW, &tv);
  			start = tv.tv_sec + tv.tv_nsec * 1e-9;
  		}
  		char buf[32];
  		lseek(fd, 0, 0);
  		int n = read(fd, buf, 32);
 		if (n > 0) {
 			buf[n] = 0;
 			char *o = NULL;
 			sum += strtod(buf, &o);
 			cnt += 1;
 		}
 		if (cnt >= 1000) {
 			struct timespec tv;
 			clock_gettime(CLOCK_MONOTONIC_RAW, &tv);
 			double end = tv.tv_sec + tv.tv_nsec * 1e-9;
 			//fprintf(stderr, "Read %d values in %.3f milliseconds\n", cnt, (end - start) * 1000);
 			fprintf(fp, "%.3f\n", sum / cnt);
			fflush(fp);
 			cnt = 0;
 			sum = 0;
 		}
 	}
}

void single_power_loop(const string &mode, const string &title) {
	if (pc_map.find(mode) != pc_map.end()) {
		string found = pc_map[mode];
		int fd = Open(found.c_str(), O_RDONLY | O_NONBLOCK);
		string out_name = title + "_" + mode + ".txt";
		printf("%s\n", out_name.c_str());
		FILE *fp = fopen(out_name.c_str(), "w");
 		if (fp) {
 			power_consumption_loop(fd, fp);
 		}
	}
}

/**
 * Wrapper for open
 */
int Open(const char *s, int mode) {
	int fd = open(s, mode);
	if (fd < 0) {
		perror("open()");
		exit(1);
	}
	return fd;
}

void dd() {
}

/**
 * Usage: ./power <mode> title
 * mode could be wifi, soc, cpu, ddr or all.
 */
int main(int argc, char *argv[]) {
	pc_map.insert(pair<string, string>("gpu",
	"/sys/devices/3160000.i2c/i2c-0/0-0040/iio_device/in_power0_input"));
	pc_map.insert(pair<string, string>("soc",
	"/sys/devices/3160000.i2c/i2c-0/0-0040/iio_device/in_power1_input"));
	pc_map.insert(pair<string, string>("wifi",
	"/sys/devices/3160000.i2c/i2c-0/0-0040/iio_device/in_power2_input"));
	pc_map.insert(pair<string, string>("cpu",
	"/sys/devices/3160000.i2c/i2c-0/0-0041/iio_device/in_power1_input"));
	pc_map.insert(pair<string, string>("ddr",
	"/sys/devices/3160000.i2c/i2c-0/0-0041/iio_device/in_power2_input"));

	const string mode = string(argv[1]);
	const string title = string(argv[2]);

	if (argc != 3) {
		fprintf(stderr, "Please enter the mode.\n");
		exit(1);
	} else {
		if (mode == "all") {
			vector<thread> t_vec;
			for (auto &m : pc_map) {
				t_vec.push_back(thread(single_power_loop, m.first, title));
			}
			for (auto &t : t_vec) {
				t.join();
			}
		} else {
			single_power_loop(mode, title);
		}
	}

	return 0;
}

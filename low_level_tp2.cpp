#include <chrono>
#include <condition_variable>
#include <iostream>
#include <mutex>
#include <queue>
#include <thread>
#include <vector>

struct Task {
  int identifier;
  int size;
  double time_taken;

  void work() {

    std::this_thread::sleep_for(std::chrono::milliseconds(size));
    time_taken = size / 1000.0;
  }
};

// 2. LE QUEUE MANAGER (Thread-Safe Queue)

template <typename T> class SafeQueue {
private:
  std::queue<T> queue;
  std::mutex mtx;
  std::condition_variable cv;

public:
  void push(T item) {
    std::unique_lock<std::mutex> lock(mtx);
    queue.push(item);
    cv.notify_one();
  }

  bool pop(T &item) {
    std::unique_lock<std::mutex> lock(mtx);
    cv.wait(lock, [this]() { return !queue.empty(); });

    item = queue.front();
    queue.pop();
    return true;
  }
};

SafeQueue<Task> task_queue;
SafeQueue<Task> result_queue;

void minion(int id) {
  while (true) {
    Task t;
    task_queue.pop(t);

    if (t.identifier == -1)
      break;

    t.work();

    result_queue.push(t);

    printf("Minion %d finished Task %d\n", id, t.identifier);
  }
}

int main() {
  int num_tasks = 20;
  int num_minions = std::thread::hardware_concurrency(); // cpu_count

  std::vector<std::thread> minions;

  std::cout << "Boss: Hiring " << num_minions << " minions..." << std::endl;

  for (int i = 0; i < num_minions; ++i) {
    minions.emplace_back(minion, i);
  }

  std::cout << "Boss: Distributing work..." << std::endl;
  for (int i = 0; i < num_tasks; ++i) {
    Task t;
    t.identifier = i;
    t.size = 10 + (i * 5);
    task_queue.push(t);
  }

  for (int i = 0; i < num_minions; ++i) {
    Task stop_signal;
    stop_signal.identifier = -1;
    task_queue.push(stop_signal);
  }

  std::cout << "Boss: Waiting for results..." << std::endl;
  for (int i = 0; i < num_tasks; ++i) {
    Task result;
    result_queue.pop(result);
    std::cout << "  Task " << result.identifier << " done in "
              << result.time_taken << "s" << std::endl;
  }

  for (auto &m : minions) {
    m.join();
  }

  std::cout << "Boss: All done." << std::endl;
  return 0;
}

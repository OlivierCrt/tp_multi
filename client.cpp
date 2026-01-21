#include <cpr/cpr.h>
#include <iostream>
#include <nlohmann/json.hpp>
#include <vector>

using json = nlohmann::json;

int main() {
  // 1. Création des données (similaire à Task.__init__)
  int size = 10;
  std::vector<double> b(size, 1.0);
  std::vector<std::vector<double>> a(size, std::vector<double>(size, 0.0));

  // Création d'une matrice diagonale simple pour le test
  for (int i = 0; i < size; i++) {
    a[i][i] = 2.0;
  }

  // 2. Construction du JSON
  json j;
  j["identifier"] = 1;
  j["size"] = size;
  j["a"] = a;
  j["b"] = b;
  j["x"] = std::vector<double>(size, 0.0); // Placeholder
  j["time"] = 0.0;

  // 3. Envoi au serveur Python
  std::cout << "Sending request to http://localhost:8000..." << std::endl;
  cpr::Response r =
      cpr::Post(cpr::Url{"http://localhost:8000"}, cpr::Body{j.dump()},
                cpr::Header{{"Content-Type", "application/json"}});

  // 4. Réception et affichage
  if (r.status_code == 200) {
    json response = json::parse(r.text);
    std::cout << "Solution received!" << std::endl;
    std::cout << "Time taken by Python: " << response["time"] << "s"
              << std::endl;

    std::vector<double> x = response["x"];
    std::cout << "First element of x: " << x[0] << std::endl;
  } else {
    std::cerr << "Error: " << r.status_code << std::endl;
  }

  return 0;
}

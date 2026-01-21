cmake_minimum_required(VERSION 3.14)
project(tp_multi_client)

set(CMAKE_CXX_STANDARD 17)

include(FetchContent)

# Téléchargement automatique de CPR (Requêtes HTTP)
FetchContent_Declare(
  cpr
  GIT_REPOSITORY https://github.com/libcpr/cpr.git
  GIT_TAG        1.10.5
)
FetchContent_MakeAvailable(cpr)

# Téléchargement automatique de JSON
FetchContent_Declare(json
    GIT_REPOSITORY https://github.com/nlohmann/json.git
    GIT_TAG        v3.11.3)
FetchContent_MakeAvailable(json)

add_executable(client client.cpp)
target_link_libraries(client PRIVATE cpr::cpr nlohmann_json::nlohmann_json)

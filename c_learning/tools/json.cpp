#include <iostream>
#include <nlohmann/json.hpp>

// 使用nlohmann/json库的命名空间
using json = nlohmann::json;

// 用于在控制台中打印JSON对象的递归函数
void printJson(const json& j, const std::string& prefix = "", const std::string& indent = "  ") {
    switch (j.type()) {
        case json::value_t::object:
            for (auto it = j.begin(); it != j.end(); ++it) {
                std::cout << prefix << it.key() << " : ";
                printJson(it.value(), prefix + indent, indent);
            }
            break;
        case json::value_t::array:
            std::cout << prefix << "[" << std::endl;
            for (const auto& elem : j) {
                printJson(elem, prefix + indent, indent);
            }
            std::cout << prefix << "]" << std::endl;
            break;
        case json::value_t::string:
            std::cout << prefix << j.get<std::string>() << std::endl;
            break;
        case json::value_t::number_integer:
            std::cout << prefix << j.get<int>() << std::endl;
            break;
        case json::value_t::number_float:
            std::cout << prefix << j.get<double>() << std::endl;
            break;
        case json::value_t::boolean:
            std::cout << prefix << (j.get<bool>() ? "true" : "false") << std::endl;
            break;
        case json::value_t::null:
            std::cout << prefix << "null" << std::endl;
            break;
        case json::value_t::discarded:
            std::cout << prefix << "discarded" << std::endl;
            break;
        default:
            break;
    }
}

int main() {
    // 创建一个JSON对象
    json j;
    j["name"] = "John Doe";
    j["age"] = 30;
    j["is_student"] = false;
    j["grades"] = {88, 92, 79};
    j["address"]["street"] = "123 Main St";
    j["address"]["city"] = "Anytown";

    // 序列化JSON对象
    std::string serialized = j.dump(4); // 4是缩进级别
    std::cout << "Serialized JSON:\n" << serialized << std::endl;

    // 反序列化JSON字符串
    json deserialized = json::parse(serialized);

    // 可视化打印JSON对象
    std::cout << "\nVisualized JSON:\n";
    printJson(deserialized);

    return 0;
}
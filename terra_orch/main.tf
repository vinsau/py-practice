provider "random" {}

resource "random_pet" "my_name" {
    length = 2
}

output "pet_name" {
    value = random_pet.my_name.i
}
from .parse_terraform import parse_output

failure = """docker_image.nginx: Refreshing state... [id=sha256:81be38025ss9476d1b7303cb575df80e419fd1b3be4a639f3b3e51cf95720c7bnginx]
docker_container.nginx: Refreshing state... [id=fca2160486f0dab6d5fda6cfa1608b465b203b8a4a57ad379d19b383f1221235]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  - destroy

Terraform will perform the following actions:

# aws_iam_user.test-mario will be created
+ resource "aws_iam_user" "test-mario" {
+ arn           = (known after apply)
+ force_destroy = false
+ id            = (known after apply)
+ name          = "test-mario"
+ path          = "/"
+ tags_all      = (known after apply)
+ unique_id     = (known after apply)
}

# docker_image.nginx will be destroyed
# (because docker_image.nginx is not in configuration)
- resource "docker_image" "nginx" {
- id           = "sha256:81be38025439476d1b7303cb575df80e419fd1sbbe4a639f3b3e51cf95720c7bnginx" -> null
- image_id     = "sha256:81be38025439476d1b7303cb575df80e4ff89zfd1b3be4a639f3b3e51cf95720c7b" -> null
- keep_locally = false -> null
- name         = "nginx" -> null
- repo_digest  = "nginx@sha256:86e53c4c16a6a276b204b0fd3a8143as6547c967dc8258b3d47c3a21bb68d3c6" -> null
}

Plan: 1 to add, 0 to change, 1 to destroy."""


def test_parse_create_and_destroy():
    expected = ["aws_iam_user.test-mario will be created", "docker_image.nginx will be destroyed",
                "(because docker_image.nginx is not in configuration)"]
    lines = failure.split('\n')
    lines.reverse()
    results = parse_output(lines)
    assert results == expected


aws_error = """Do you want to perform these actions?
Terraform will perform the actions described above.
Only 'yes' will be accepted to approve.

Enter a value: yes

docker_image.nginx: Destroying... [id=sha256:81be38025439476d1b7303cb575df80e419fd1b3be4a639f3b3e51cf95720c7bnginx]
docker_image.nginx: Destruction complete after 1s
aws_iam_user.test-mario: Creating...
╷
│ Error: creating IAM User (test-mario): EntityAlreadyExists: User with name test-mario already exists.
│ 	status code: 409, request id: fds444-a507-4593-997d-112sw
│
│   with aws_iam_user.test-mario,
│   on main.tf line 16, in resource "aws_iam_user" "test-mario":
│   16: resource "aws_iam_user" "test-mario" {
│
╵"""


def test_parse_aws_error():
    expected = [
        "Error creating IAM User (test-mario): EntityAlreadyExists: User with name test-mario already exists.",
        "line 16"]
    lines = aws_error.split('\n')
    lines.reverse()
    results = parse_output(lines)
    assert results == expected


two_aws_error = """Do you want to perform these actions?
Terraform will perform the actions described above.
Only 'yes' will be accepted to approve.

  Enter a value: yes

aws_iam_user.mario: Creating...
aws_iam_user.test-mario: Creating...
╷
│ Error: creating IAM User (test-mario): EntityAlreadyExists: User with name test-mario already exists.
│       status code: 409, request id: f33r-9080-47f4-9e99-112sw232
│ 
│   with aws_iam_user.test-mario,
│   on main.tf line 16, in resource "aws_iam_user" "test-mario":
│   16: resource "aws_iam_user" "test-mario" {
│ 
╵
╷
│ Error: creating IAM User (mario): EntityAlreadyExists: User with name mario already exists.
│       status code: 409, request id: dsa455-c749-4769-868d-352dss
│ 
│   with aws_iam_user.mario,
│   on main.tf line 20, in resource "aws_iam_user" "mario":
│   20: resource "aws_iam_user" "mario" {
│ 
╵
"""


def test_parse_two_aws_error():
    expected = [
        "Error creating IAM User (test-mario): EntityAlreadyExists: User with name test-mario already exists.",
        "line 16",
        "Error creating IAM User (mario): EntityAlreadyExists: User with name mario already exists.", "line 20"]
    lines = two_aws_error.split('\n')
    lines.reverse()
    results = parse_output(lines)
    assert results == expected


syntax_error = """╷
│ Error: Unsupported block type
│
│   on main.tf line 12:
│   12: resoure "docker_image" "nginx" {
│
│ Blocks of type "resoure" are not expected here. Did you mean "resource"?"""


def test_syntax_error():
    expected = ["Error Unsupported block type", "line 12",
                'Blocks of type "resoure" are not expected here. Did you mean "resource"?']
    lines = syntax_error.split('\n')
    lines.reverse()
    results = parse_output(lines)
    assert results == expected

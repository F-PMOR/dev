# ANSIBLE



## FILE

* instancier un variable avec la valeur d'un fichier ou par donner une valeur par defaut.
```
__ohrassertToken: "{{ lookup('ansible.builtin.file', '~/.vault-token', errors='ignore')| from_yaml | default('NA',true) }}"
```
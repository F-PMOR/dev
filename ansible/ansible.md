# ANSIBLE



## FILE

* instancier un variable avec le contenu d'un fichier ou une valeur par defaut.
```
__ohrassertToken: "{{ lookup('ansible.builtin.file', '~/.vault-token', errors='ignore')| from_yaml | default('NA',true) }}"
```

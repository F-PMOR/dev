# ANSIBLE



## FILE

* instancier un variable avec le contenu d'un fichier ou une valeur par defaut.
```
__ohrassertToken: "{{ lookup('ansible.builtin.file', '~/.vault-token', errors='ignore')| from_yaml | default('NA',true) }}"
```


## BLOCK
  * on ne peut utiliser les blocks que dans des tasks, pas dans un role !
  exemple, ceci ne marche pas
  ```
  roles:
    - name: Assertion with collection
      block:
        - name: assertions variable
          role: pmorry.assertions.first
          vars:
            vars_are_defined:
              - toto
              - titi
            fail_msg: "le nom du 'device' doit être passé en extra paramètre (-e CI_DEVICE) avec le playbook"
      ignore_errors: yes
  ```
  Il faut utiliser : 
  ```
    tasks:
    - name: Assertion with collection
      ansible.builtin.import_role:
        name: pmorry.assertions.first
      vars:
        vars_are_defined:
          - toto
          - titi
        fail_msg: "le nom du 'device' doit être passé en extra paramètre (-e CI_DEVICE) avec le playbook"
      ignore_errors: yes
  ```
  
  

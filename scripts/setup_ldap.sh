# scripts/setup_ldap.sh

#!/bin/bash

# Create the organizational units
docker exec ldap-server bash -c "ldapadd -x -H ldap://localhost \
  -D 'cn=admin,dc=company,dc=com' \
  -w admin123 << EOF
dn: ou=users,dc=company,dc=com
objectClass: organizationalUnit
ou: users

dn: ou=groups,dc=company,dc=com
objectClass: organizationalUnit
ou: groups
EOF"

echo "[SUCCESS] LDAP structure initialized"


# Verify structure was created
docker exec ldap-server ldapsearch -x -H ldap://localhost \
  -b "dc=company,dc=com" \
  -D "cn=admin,dc=company,dc=com" \
  -w admin123 \
  "(objectClass=organizationalUnit)"
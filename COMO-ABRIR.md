# 🚀 Como Visualizar a Landing Page Salus

## Método 1: Abertura Direta (Mais Simples)

1. **Localize o arquivo** `salus-copy-landing.html` na pasta do projeto
2. **Clique duplo** no arquivo para abrir no seu navegador padrão
3. **Pronto!** A landing page será carregada com todas as funcionalidades

## Método 2: Servidor Local (Recomendado para Desenvolvimento)

### Se você tem Python instalado:
```bash
# Navegue até a pasta do projeto
cd /caminho/para/pasta/do/projeto

# Python 3
python -m http.server 8000

# Ou Python 2
python -m SimpleHTTPServer 8000

# Abra no navegador: http://localhost:8000/salus-copy-landing.html
```

### Se você tem Node.js instalado:
```bash
# Instale o servidor simples
npm install -g http-server

# Navegue até a pasta
cd /caminho/para/pasta/do/projeto

# Inicie o servidor
http-server

# Abra no navegador: http://localhost:8080/salus-copy-landing.html
```

## Método 3: Live Server (VS Code)

1. **Instale a extensão** "Live Server" no VS Code
2. **Abra a pasta** do projeto no VS Code
3. **Clique direito** no arquivo `salus-copy-landing.html`
4. **Selecione** "Open with Live Server"
5. **Automaticamente** abrirá no navegador com hot reload

---

## 📱 Testando em Dispositivos Móveis

### Usando o mesmo WiFi:
1. **Descubra seu IP local** (ex: 192.168.1.100)
2. **Acesse pelo celular**: `http://192.168.1.100:8000/salus-copy-landing.html`
3. **Teste** todas as funcionalidades touch

### Usando DevTools:
1. **Abra** Chrome DevTools (F12)
2. **Clique** no ícone de dispositivo móvel
3. **Selecione** diferentes tamanhos de tela
4. **Teste** responsividade

---

## 🔧 Resolução de Problemas

### **Animações não funcionam:**
- ✅ Verifique se o arquivo `salus-advanced-features.js` está na mesma pasta
- ✅ Abra o Console (F12) e veja se há erros
- ✅ Certifique-se de que JavaScript está habilitado

### **Fontes não carregam:**
- ✅ Verifique sua conexão com internet
- ✅ Google Fonts precisa de internet para carregar
- ✅ Em caso offline, as fontes padrão serão usadas

### **Performance lenta:**
- ✅ Use um navegador moderno (Chrome, Firefox, Safari, Edge)
- ✅ Feche outras abas para liberar memória
- ✅ Em dispositivos antigos, algumas animações podem ser reduzidas automaticamente

---

## 🎯 Navegadores Suportados

### **Totalmente Suportados:**
- ✅ Chrome 80+
- ✅ Firefox 75+
- ✅ Safari 13+
- ✅ Edge 80+

### **Parcialmente Suportados:**
- ⚠️ Internet Explorer 11 (sem animações avançadas)
- ⚠️ Navegadores móveis antigos (funcionalidade básica)

---

## 📊 Funcionalidades para Testar

### **Desktop:**
1. **Hover** nos botões (efeito magnético)
2. **Scroll** para ver animações de entrada
3. **Hover** nos cards (efeito tilt 3D)
4. **Progress bar** no topo da página
5. **Partículas animadas** no background do hero

### **Mobile:**
1. **Touch** nos botões
2. **Scroll** suave entre seções
3. **Responsividade** em diferentes orientações
4. **Performance** das animações

### **Analytics (Console):**
1. **Abra** DevTools (F12)
2. **Vá** para a aba Console
3. **Veja** os eventos sendo rastreados:
   - `scroll_depth: 25%`
   - `section_view: crisis`
   - `cta_click: QUERO PROTEGER FAMÍLIAS`

---

## 🚀 Próximos Passos

1. **Teste** em diferentes dispositivos
2. **Compartilhe** com a equipe para feedback
3. **Personalize** cores e conteúdo conforme necessário
4. **Integre** com WhatsApp Business
5. **Configure** analytics real (Google Analytics, etc.)

---

**A landing page está pronta para impressionar o CEO da Salus! 🎯** 
<template>

    <div v-if = "auth">

        <div class ="wrapper">
                <div class =  "leftSideFunctionsArea">

                    <div class  = "homePersonalProfile">
                        <img class="img" style= "border-radius: 50%;" src="../assets/images/profilepic.png" />

                    </div>


                    <div class = "leftAllFunction">
                        <p>{{message}}</p>

                        <div class  = "leftFunctions">

                            <div class  = "functionLink">
                                <a href ="#">
                                    <Icon icon="clarity:users-line" style="color: #171b72;" width="40" height="40"/>Friend
                                </a>
                            </div>

                            <div class  = "functionLink">
                                <a href ="#">
                                    <Icon icon="bx:archive-in" style="color: #171b72;" width="40" height="40"/>Archive
                                </a>
                            </div>

                            <div class  = "functionLink">
                                <a href ="/#/changePassword">
                                    <Icon icon="ic:twotone-lock-reset" style="color: #171b72;" width="40" height="40"/>Reset Password
                                </a>
                            </div>


                            <div class  = "functionLink">
                                <a href ="#" @click = "logout()">
                                    <Icon icon="heroicons-outline:logout" style="color: #171b72;" width="40" height="40"/>Log out
                                </a>
                            </div>

                        </div>

                        <div class  = "leftFunctionsFilter">

                            <div class = "categoryFilter">
                                <h3>Category</h3>
                                <div v-for = "item in genreList">
                                    <label class="container">{{item.name}}
                                        <input type="checkbox"
                                        v-model="checkedTypes1"
                                        :value="item.id"
                                        >
                                        <span class="checkmark"></span>
                                    </label>
                                </div>

                            </div>


                        </div>

                    </div>



                </div>

                <div class = "centralFunctionsArea">
                    <div class = "navigationBar">

                        <div class = "navigationBar-Button">
                            <nav>
                                <a href="/#/" class="hover-underline-animation">
                                    Own Post
                                </a>
                            </nav>

                        </div>
                        <div class = "navigationBar-Button">
                            <nav>
                                <a href="#" class="hover-underline-animation">
                                    Friend Post
                                </a>
                                </nav>

                        </div>
                        <div class = "navigationBar-Button">
                            <nav>
                                <a href="/#/allPublicPost" class="hover-underline-animation::after">
                                    Square
                                </a>
                                </nav>

                        </div>

                    </div>

                    <div class = "post-wrapper">
                        <div class = "allPosts"

                        v-for = "post in filteredPosts.slice().reverse()"
                        v-bind:key = "post.records_id"
                        >

                            <div v-if = "post.privacy == 'public'">
                                <div class = "post">
                                    <div class = "post-Left">
                                        <img :src="require(`@/assets/${editRoot(post.thumbnail)}`)"  class = "thumbnail"/>
                                    </div>

                                    <div class = "post-Right">
                                        <div class = "info">
                                            <div class ="title">
                                                <a :href = "'/#/record/' + post.records_id">{{post.title}}</a>
                                            </div>

                                            <div class ="author">
                                                {{post.artist}}
                                            </div>

                                            <div class ="read">
                                                Read in: 2022

                                            </div>


                                            <div class ="score">

                                                <div v-for="index in post.rate" :key="index">
                                                    <span class="fa fa-star" style="color: #FFCB45;"></span>
                                                </div>

                                                <div v-for="index in 5 - post.rate" :key="index">
                                                    <span class="fa fa-star" style="color: #F2F2F2;"></span>
                                                </div>


                                            </div>

                                            <div class ="comment">
                                                {{post.comment}}
                                            </div>

                                        </div>

                                        <div class = "postOperation">


                                        </div>

                                    </div>

                                </div>
                            </div>


                        </div>
                    </div>


                </div>

                <div class = "rightSideFunctionsArea">
                    <div class = "search">
                        <input type="text" id ="inputText" class="mySearch" placeholder="Search.." v-model = "search">
                    </div>

                    <div class = "addPost">
                        <a href ="/#/posts">
                            <Icon class = "newPostIcon" icon="fluent:add-circle-32-filled"/>New Post
                        </a>
                    </div>


                </div>

        </div>

        <div class = "bubblefooter">
            <div class="footer">
                <div class="bubbles">
                    <div class="bubble" style="--size:3.1201303650884444rem; --distance:6.820093960838137rem; --position:82.34721175392593%; --time:2.0206203438296235s; --delay:-2.7843512720490526s;"></div>
                    <div class="bubble" style="--size:4.1395058299797824rem; --distance:8.921665829525018rem; --position:79.38889096959407%; --time:3.9475852323941067s; --delay:-3.222658307928825s;"></div>
                    <div class="bubble" style="--size:5.840444833065807rem; --distance:8.23625607479463rem; --position:39.1044965058931%; --time:3.466106968071153s; --delay:-2.1723165018623494s;"></div>
                    <div class="bubble" style="--size:4.966510326572795rem; --distance:6.5730607797771485rem; --position:104.23906974630908%; --time:2.90553204109787s; --delay:-3.5949357170184713s;"></div>
                    <div class="bubble" style="--size:4.86183549631585rem; --distance:6.242682674016914rem; --position:65.63742427360468%; --time:3.240989496191238s; --delay:-3.9184007190159873s;"></div>
                    <div class="bubble" style="--size:4.193283988224256rem; --distance:9.583432012282504rem; --position:16.39507986777308%; --time:2.095485412182945s; --delay:-2.0236333002845512s;"></div>
                    <div class="bubble" style="--size:2.377656025966316rem; --distance:6.538586246474145rem; --position:103.52813904304855%; --time:3.8233309309348846s; --delay:-2.1280438951882155s;"></div>
                    <div class="bubble" style="--size:4.100680588632886rem; --distance:8.019764466805439rem; --position:22.506192993118404%; --time:3.6535480198488726s; --delay:-2.236112011234188s;"></div>
                    <div class="bubble" style="--size:3.5981777530937684rem; --distance:6.583023721585926rem; --position:49.201184071695586%; --time:2.9791720268621185s; --delay:-2.5492942978119273s;"></div>
                    <div class="bubble" style="--size:4.999255904761137rem; --distance:7.272008733506542rem; --position:4.443958761151826%; --time:3.2923226076852523s; --delay:-3.535072912393939s;"></div>
                    <div class="bubble" style="--size:2.7756353927808615rem; --distance:7.072385164856592rem; --position:103.97033318338833%; --time:3.0176020222567477s; --delay:-3.1422619651416346s;"></div>
                    <div class="bubble" style="--size:3.9669377460899513rem; --distance:9.937979735086822rem; --position:68.05494175605817%; --time:2.340016958793365s; --delay:-2.577515550354831s;"></div>
                    <div class="bubble" style="--size:4.921385214885162rem; --distance:9.989142917719438rem; --position:39.0663510711938%; --time:3.3929779935229893s; --delay:-3.4939410204689088s;"></div>
                    <div class="bubble" style="--size:3.6086011045282067rem; --distance:7.968932941153643rem; --position:76.25710383551254%; --time:3.6380560572244676s; --delay:-2.7837278925629656s;"></div>
                    <div class="bubble" style="--size:4.651547007788648rem; --distance:6.859976759023908rem; --position:21.837105643327014%; --time:2.2958646236300573s; --delay:-2.9352367931212497s;"></div>
                    <div class="bubble" style="--size:5.62872682946968rem; --distance:7.933977075494613rem; --position:-0.17506889850420215%; --time:3.619098365083033s; --delay:-2.197030511903673s;"></div>
                    <div class="bubble" style="--size:4.243076968066346rem; --distance:9.594382496061785rem; --position:15.725673265787993%; --time:2.551770821743508s; --delay:-2.4486678391344627s;"></div>
                    <div class="bubble" style="--size:4.726926239733698rem; --distance:6.7706454521543735rem; --position:13.582997051967858%; --time:3.941675397472705s; --delay:-2.120101896029822s;"></div>
                    <div class="bubble" style="--size:3.3156903458552964rem; --distance:7.558087931688566rem; --position:18.06897889931619%; --time:2.306099997053957s; --delay:-3.8702404480222348s;"></div>
                    <div class="bubble" style="--size:5.388090164607011rem; --distance:8.631693184141199rem; --position:41.82854320280728%; --time:2.2832879729852005s; --delay:-3.1386925815380393s;"></div>
                    <div class="bubble" style="--size:4.618393454831297rem; --distance:9.386432139029957rem; --position:-3.6072595933362894%; --time:3.7161912919647886s; --delay:-3.905490438885363s;"></div>
                    <div class="bubble" style="--size:2.6826629712877628rem; --distance:8.651262495622875rem; --position:63.83376773458511%; --time:2.3191700291543498s; --delay:-2.720638950205651s;"></div>
                    <div class="bubble" style="--size:5.769713650731845rem; --distance:9.584408417531355rem; --position:103.13812052427411%; --time:2.211558109004075s; --delay:-3.7174025135365123s;"></div>
                    <div class="bubble" style="--size:4.709109033733652rem; --distance:7.8721609141254545rem; --position:104.09972749948764%; --time:2.176806595725826s; --delay:-3.877310062809512s;"></div>
                    <div class="bubble" style="--size:3.9507296573326993rem; --distance:7.582557160142883rem; --position:98.31550484837966%; --time:3.2420854678093844s; --delay:-3.4120087271488027s;"></div>
                    <div class="bubble" style="--size:3.208290292100582rem; --distance:6.601311146423942rem; --position:78.9540985008481%; --time:3.8334380025269335s; --delay:-3.11096301433526s;"></div>
                    <div class="bubble" style="--size:3.8532271720570677rem; --distance:7.959321748077524rem; --position:12.013085970739624%; --time:3.5416890677722264s; --delay:-2.1359262351486707s;"></div>
                    <div class="bubble" style="--size:2.542454225068842rem; --distance:9.521201049056465rem; --position:82.10922765883362%; --time:3.581579180028622s; --delay:-3.999373673578908s;"></div>
                    <div class="bubble" style="--size:5.454187349497576rem; --distance:9.95250695582811rem; --position:38.772739090786224%; --time:2.498707449992124s; --delay:-3.7544118711743084s;"></div>
                    <div class="bubble" style="--size:5.8525882546497865rem; --distance:8.896776049198344rem; --position:12.665488030797341%; --time:2.327408248154069s; --delay:-2.787651632117573s;"></div>
                    <div class="bubble" style="--size:4.6773294925241355rem; --distance:9.382328554878221rem; --position:88.01930113173296%; --time:3.5193859957802656s; --delay:-3.0370716142889314s;"></div>
                    <div class="bubble" style="--size:5.1784913794379825rem; --distance:7.646670413564143rem; --position:59.221892814153094%; --time:2.963516599738071s; --delay:-3.0218897880386164s;"></div>
                    <div class="bubble" style="--size:3.3349069002336584rem; --distance:9.073419129598516rem; --position:10.82787248937241%; --time:3.1180685604767526s; --delay:-3.477630874995105s;"></div>
                    <div class="bubble" style="--size:3.9232684544481717rem; --distance:8.595851123506506rem; --position:25.50893500566246%; --time:2.2866548947774414s; --delay:-2.3534746901683823s;"></div>
                    <div class="bubble" style="--size:4.976688725973153rem; --distance:7.937835186207333rem; --position:91.66029510536619%; --time:2.1126188213058152s; --delay:-2.5961295690639106s;"></div>
                    <div class="bubble" style="--size:4.567659807297635rem; --distance:7.410786484043222rem; --position:58.11170778671322%; --time:2.0051783993961627s; --delay:-2.86809491862578s;"></div>
                    <div class="bubble" style="--size:4.23820394378414rem; --distance:8.490291355669767rem; --position:80.08071924614744%; --time:2.749390131376655s; --delay:-3.5976420245798963s;"></div>
                    <div class="bubble" style="--size:2.8422177554248282rem; --distance:6.0692710838629536rem; --position:85.72793452759218%; --time:3.364174241046546s; --delay:-3.70782438585065s;"></div>
                    <div class="bubble" style="--size:4.699180529888344rem; --distance:9.496236163924907rem; --position:103.70871301650622%; --time:2.9106749438720065s; --delay:-3.194032684638041s;"></div>
                    <div class="bubble" style="--size:2.333569513864256rem; --distance:8.96721896606003rem; --position:40.146649267881294%; --time:2.0969338050321964s; --delay:-3.002398942798994s;"></div>
                    <div class="bubble" style="--size:4.723733489337293rem; --distance:9.666270145644408rem; --position:2.6485677504097094%; --time:3.7496795995292422s; --delay:-3.677680515244844s;"></div>
                    <div class="bubble" style="--size:2.610582438009734rem; --distance:9.442905988465068rem; --position:50.50521166279105%; --time:3.541300676985273s; --delay:-2.020640915964908s;"></div>
                    <div class="bubble" style="--size:3.7751434863792817rem; --distance:6.409087376799411rem; --position:1.5101222057030288%; --time:2.1037390458503844s; --delay:-3.0488902368953s;"></div>
                    <div class="bubble" style="--size:2.401597773124016rem; --distance:9.169041315327021rem; --position:0.500806106907743%; --time:3.703496959120544s; --delay:-2.706507098569315s;"></div>
                    <div class="bubble" style="--size:2.2503016300493677rem; --distance:6.893846249897305rem; --position:1.3664003771843642%; --time:2.4727084742829573s; --delay:-2.163450515576659s;"></div>
                    <div class="bubble" style="--size:3.78204410225825rem; --distance:8.935620719624868rem; --position:78.68733224938106%; --time:3.893425356108055s; --delay:-2.6953052062580927s;"></div>
                    <div class="bubble" style="--size:3.4761581213464128rem; --distance:6.498174714655941rem; --position:101.27745849462735%; --time:3.3049400595338003s; --delay:-3.361129282417892s;"></div>
                    <div class="bubble" style="--size:4.464743890911591rem; --distance:6.580742878241696rem; --position:24.520611565952628%; --time:2.726129827470934s; --delay:-3.187400474906847s;"></div>
                    <div class="bubble" style="--size:3.243700274424662rem; --distance:6.353743461481931rem; --position:22.58105287084379%; --time:3.0921966707056083s; --delay:-2.714571849014212s;"></div>
                    <div class="bubble" style="--size:5.48318913269727rem; --distance:7.610516016440386rem; --position:73.00026719092631%; --time:2.152293624282368s; --delay:-2.1093334360323253s;"></div>
                    <div class="bubble" style="--size:3.959819502992824rem; --distance:9.747247515725206rem; --position:90.48032199008617%; --time:3.1013902994957916s; --delay:-2.5808949699486243s;"></div>
                    <div class="bubble" style="--size:5.90543854110207rem; --distance:7.500964374344243rem; --position:-4.885672769774967%; --time:3.535481129544745s; --delay:-2.6689485473862224s;"></div>
                    <div class="bubble" style="--size:5.6112849530017rem; --distance:9.279325193489012rem; --position:102.19478120480564%; --time:3.472515960121058s; --delay:-2.5001218365506483s;"></div>
                    <div class="bubble" style="--size:3.589150715242858rem; --distance:9.844660199666588rem; --position:1.2970253837915706%; --time:3.3134220398170044s; --delay:-2.2393676565056295s;"></div>
                    <div class="bubble" style="--size:4.499144154222871rem; --distance:9.405327485195844rem; --position:79.12578552805223%; --time:3.280704909783962s; --delay:-3.212712998606146s;"></div>
                    <div class="bubble" style="--size:4.021139013684823rem; --distance:6.142455614154008rem; --position:35.48170592116572%; --time:3.6841729886125028s; --delay:-3.414839085881087s;"></div>
                    <div class="bubble" style="--size:5.031841577045535rem; --distance:8.032694319316345rem; --position:3.205110511139919%; --time:2.947027899527258s; --delay:-2.181129572037044s;"></div>
                    <div class="bubble" style="--size:4.975721270584174rem; --distance:9.108235090392128rem; --position:64.70373439227399%; --time:2.6471410300612668s; --delay:-3.8761720664756996s;"></div>
                    <div class="bubble" style="--size:5.026766485106916rem; --distance:7.15513251813021rem; --position:11.117840373693074%; --time:3.3425447416655074s; --delay:-3.4457526722257756s;"></div>
                    <div class="bubble" style="--size:5.174281526251692rem; --distance:9.533111364051589rem; --position:32.77648502537066%; --time:2.5558540698351466s; --delay:-3.5423504911851573s;"></div>
                    <div class="bubble" style="--size:5.3701297454386445rem; --distance:9.940027205178225rem; --position:60.98407942057652%; --time:3.5538605780954953s; --delay:-3.27313518292343s;"></div>
                    <div class="bubble" style="--size:3.7837090906289372rem; --distance:7.208473022166191rem; --position:103.29544830203697%; --time:3.0792124825386558s; --delay:-2.8494041213513546s;"></div>
                    <div class="bubble" style="--size:5.699737568051859rem; --distance:6.619301631720345rem; --position:23.853428192767247%; --time:2.0975335622177176s; --delay:-3.678323411902189s;"></div>
                    <div class="bubble" style="--size:5.729364492036976rem; --distance:6.863397626666973rem; --position:47.332609750631576%; --time:3.3087665821029733s; --delay:-2.0557803748409946s;"></div>
                    <div class="bubble" style="--size:2.847608055761145rem; --distance:7.377139468326187rem; --position:32.78055964668272%; --time:3.637188403170763s; --delay:-3.5282707866198315s;"></div>
                    <div class="bubble" style="--size:2.1611128307315033rem; --distance:6.956884363522469rem; --position:33.887668519411676%; --time:3.639994552673266s; --delay:-3.3256595458540863s;"></div>
                    <div class="bubble" style="--size:3.286782343165937rem; --distance:6.890032177817559rem; --position:48.636954983071725%; --time:3.711395411906872s; --delay:-3.0643651931372995s;"></div>
                    <div class="bubble" style="--size:4.212159571515809rem; --distance:8.01601005473157rem; --position:50.807074401176436%; --time:3.3528708646054937s; --delay:-2.6849702553846124s;"></div>
                    <div class="bubble" style="--size:4.829873710136734rem; --distance:9.008591715690539rem; --position:87.02970032186508%; --time:2.090429810059111s; --delay:-3.509770420376037s;"></div>
                    <div class="bubble" style="--size:3.129982714562014rem; --distance:7.128213288534713rem; --position:83.56060012938211%; --time:2.8271672574872024s; --delay:-3.5336078141964347s;"></div>
                    <div class="bubble" style="--size:3.4007668272506653rem; --distance:9.240094338940747rem; --position:-0.4319396993185336%; --time:2.793937117225086s; --delay:-2.8300836137430556s;"></div>
                    <div class="bubble" style="--size:4.845807898776166rem; --distance:8.17418257755508rem; --position:89.4366120287263%; --time:2.4637683441350466s; --delay:-3.9348566748169196s;"></div>
                    <div class="bubble" style="--size:2.7689328152043586rem; --distance:7.21573855601018rem; --position:56.26947929521841%; --time:2.912485055238819s; --delay:-2.026910060240969s;"></div>
                    <div class="bubble" style="--size:2.1746313507944057rem; --distance:6.314673000011655rem; --position:21.96407252854236%; --time:2.5783112951508222s; --delay:-3.382118646229507s;"></div>
                    <div class="bubble" style="--size:5.3028102695105375rem; --distance:7.901286173894735rem; --position:3.03848853931388%; --time:2.967602745403822s; --delay:-2.6365497634579573s;"></div>
                    <div class="bubble" style="--size:5.173865261491779rem; --distance:7.143069661125453rem; --position:46.3186497027009%; --time:2.781383836884853s; --delay:-3.33112471646961s;"></div>
                    <div class="bubble" style="--size:5.260765133121335rem; --distance:8.286233858232258rem; --position:95.80852775482079%; --time:3.9539955880863977s; --delay:-2.456396691736231s;"></div>
                    <div class="bubble" style="--size:4.861362779539479rem; --distance:6.348191550024412rem; --position:96.36795067950182%; --time:3.4443491150231544s; --delay:-2.039843639420512s;"></div>
                    <div class="bubble" style="--size:3.2801303492455816rem; --distance:9.59886774915357rem; --position:28.60676017060095%; --time:3.508751013763776s; --delay:-2.239108698165433s;"></div>
                    <div class="bubble" style="--size:3.683169223809993rem; --distance:9.032430036353436rem; --position:52.06131690827177%; --time:2.3814192917678634s; --delay:-3.581408618445526s;"></div>
                    <div class="bubble" style="--size:3.7979519547086626rem; --distance:8.326605881778876rem; --position:3.537796129171948%; --time:2.6666936450046923s; --delay:-2.9560659498998145s;"></div>
                    <div class="bubble" style="--size:4.06483491335709rem; --distance:7.776000767827076rem; --position:7.851179821683143%; --time:3.5890549785965735s; --delay:-2.6087922112886424s;"></div>
                    <div class="bubble" style="--size:2.141086845753824rem; --distance:9.166013506158471rem; --position:36.10685314134743%; --time:2.607876502893974s; --delay:-2.828741424194637s;"></div>
                    <div class="bubble" style="--size:4.714578886293953rem; --distance:6.775943737527767rem; --position:55.7410654349898%; --time:3.5912521997055857s; --delay:-3.548708320415166s;"></div>
                    <div class="bubble" style="--size:4.970677710237579rem; --distance:7.54621939890036rem; --position:51.769528177223435%; --time:3.8359389434753806s; --delay:-3.967635293276575s;"></div>
                    <div class="bubble" style="--size:5.732984062650092rem; --distance:9.159177718900132rem; --position:54.89747351037551%; --time:3.6402079022675657s; --delay:-3.485815499649459s;"></div>
                    <div class="bubble" style="--size:2.5643588523609457rem; --distance:8.522379508937782rem; --position:103.56502203432751%; --time:2.2355361616995544s; --delay:-2.1829440499635786s;"></div>
                    <div class="bubble" style="--size:3.0231229219818188rem; --distance:7.337293631444435rem; --position:103.77647524588016%; --time:2.011862435573944s; --delay:-2.3547765778296457s;"></div>
                    <div class="bubble" style="--size:2.784772930348785rem; --distance:6.890381886950378rem; --position:36.82166769745987%; --time:2.6134095407780147s; --delay:-2.7959469055681945s;"></div>
                    <div class="bubble" style="--size:2.2439671251386057rem; --distance:7.992594283031445rem; --position:65.60941114609066%; --time:3.9510403381480956s; --delay:-2.337019965268276s;"></div>
                    <div class="bubble" style="--size:5.882987100823751rem; --distance:6.438420682555041rem; --position:104.21131866613216%; --time:2.713505440804055s; --delay:-3.8274207828454427s;"></div>
                    <div class="bubble" style="--size:4.034848303580614rem; --distance:7.2330852248193045rem; --position:87.24363224294935%; --time:2.9762217744258184s; --delay:-3.4872348494978223s;"></div>
                    <div class="bubble" style="--size:2.031182176141587rem; --distance:8.72835019462401rem; --position:37.79960251734479%; --time:2.419379942730882s; --delay:-2.797572180759617s;"></div>
                    <div class="bubble" style="--size:4.099082391589547rem; --distance:9.771517308672625rem; --position:1.7543139224202715%; --time:3.350541429617452s; --delay:-3.287916429095983s;"></div>
                    <div class="bubble" style="--size:2.0347452354451594rem; --distance:8.97414355116221rem; --position:92.45221980584174%; --time:2.428404907003968s; --delay:-2.3377296916566133s;"></div>
                    <div class="bubble" style="--size:3.0350682136031937rem; --distance:7.895389110388747rem; --position:14.450271074922632%; --time:3.147742218232644s; --delay:-3.675393441569163s;"></div>
                    <div class="bubble" style="--size:2.5676152124765927rem; --distance:7.009455536914811rem; --position:101.24942104813758%; --time:3.3291008749518434s; --delay:-3.9077960638388274s;"></div>
                    <div class="bubble" style="--size:2.1102177372718796rem; --distance:9.504672563544329rem; --position:30.62673903191041%; --time:3.8644503019872145s; --delay:-2.444290523014626s;"></div>
                    <div class="bubble" style="--size:5.836829252469975rem; --distance:8.368726422612308rem; --position:74.32266043534244%; --time:3.815521425919984s; --delay:-2.9372351533330088s;"></div>
                    <div class="bubble" style="--size:5.442728168809156rem; --distance:6.475319247293051rem; --position:30.806910095815986%; --time:2.0982802525793183s; --delay:-3.7316824220125007s;"></div>
                    <div class="bubble" style="--size:4.836334416099813rem; --distance:9.000641182384715rem; --position:58.37869515865939%; --time:2.6698179308220777s; --delay:-2.712488321536363s;"></div>
                    <div class="bubble" style="--size:4.454915798408173rem; --distance:9.180505777960581rem; --position:8.29217566858922%; --time:2.6382430836813056s; --delay:-3.6852640145528293s;"></div>
                    <div class="bubble" style="--size:3.5373234234615083rem; --distance:6.504397194115288rem; --position:70.01827347769601%; --time:3.0327233517608416s; --delay:-3.199916529643967s;"></div>
                    <div class="bubble" style="--size:3.814636427018402rem; --distance:7.389879564335447rem; --position:63.90253786901121%; --time:2.8229931760525226s; --delay:-3.6528086909181434s;"></div>
                    <div class="bubble" style="--size:3.1471061477393976rem; --distance:9.785400585514207rem; --position:69.11575794476275%; --time:3.751286922091235s; --delay:-2.782050647121239s;"></div>
                    <div class="bubble" style="--size:4.860377406935904rem; --distance:6.860628552958142rem; --position:49.93300556429999%; --time:3.889271908552718s; --delay:-3.9043124893631966s;"></div>
                    <div class="bubble" style="--size:5.308425340205505rem; --distance:6.585125455742779rem; --position:40.85881557817584%; --time:2.672026181417905s; --delay:-2.64407835788773s;"></div>
                    <div class="bubble" style="--size:3.3564855207620887rem; --distance:9.386578969862725rem; --position:59.17477627928419%; --time:3.1131264601038544s; --delay:-3.8576340590597327s;"></div>
                    <div class="bubble" style="--size:5.765533244719809rem; --distance:6.488235000577231rem; --position:73.02571044191174%; --time:3.2544891929510107s; --delay:-2.353843026153846s;"></div>
                    <div class="bubble" style="--size:5.27783458692955rem; --distance:8.44033306962696rem; --position:22.01267355855159%; --time:3.42080595268424s; --delay:-3.215204969553316s;"></div>
                    <div class="bubble" style="--size:4.345682964256936rem; --distance:6.896633246841128rem; --position:3.524418004593027%; --time:3.728398315175406s; --delay:-3.850976737238846s;"></div>
                    <div class="bubble" style="--size:3.9195543733152336rem; --distance:6.651855825544733rem; --position:77.09624905490165%; --time:3.2561107189358967s; --delay:-2.08512069763123s;"></div>
                    <div class="bubble" style="--size:3.5267714478234993rem; --distance:7.105846489937173rem; --position:94.43121582748934%; --time:2.631214128264003s; --delay:-2.1469902149259625s;"></div>
                    <div class="bubble" style="--size:4.417175219698551rem; --distance:9.906358455103543rem; --position:81.74527081910328%; --time:3.266244547400949s; --delay:-3.19712876044915s;"></div>
                    <div class="bubble" style="--size:5.192678435669353rem; --distance:9.933073369495327rem; --position:18.85860564349444%; --time:2.6688899041026626s; --delay:-2.6286948196413147s;"></div>
                    <div class="bubble" style="--size:5.541232539840691rem; --distance:6.948958261976489rem; --position:93.47705717834523%; --time:2.9880494251170795s; --delay:-3.196833851191171s;"></div>
                    <div class="bubble" style="--size:2.0364093279734163rem; --distance:6.756557783216555rem; --position:0.765182639745583%; --time:2.5421012569066668s; --delay:-2.1141732396364157s;"></div>
                    <div class="bubble" style="--size:4.572905509419523rem; --distance:6.624447609777447rem; --position:80.66201200850678%; --time:2.2882513443772505s; --delay:-2.278060615214504s;"></div>
                    <div class="bubble" style="--size:4.7985447429332115rem; --distance:9.664189089195032rem; --position:82.63788615660026%; --time:2.657506575219055s; --delay:-2.2363451734304816s;"></div>
                    <div class="bubble" style="--size:5.239830742014584rem; --distance:6.007035168664716rem; --position:74.36548249713269%; --time:2.9087695596574945s; --delay:-2.2066702456877563s;"></div>
                    <div class="bubble" style="--size:3.645007147230875rem; --distance:7.5926170775105115rem; --position:24.034529213926582%; --time:3.8710736716167564s; --delay:-2.3491147759012314s;"></div>
                    <div class="bubble" style="--size:5.355432073466413rem; --distance:9.711888834130328rem; --position:93.82631370263447%; --time:2.0606537011443824s; --delay:-3.5485604145001295s;"></div>
                    <div class="bubble" style="--size:2.0908974486344807rem; --distance:7.346879284518681rem; --position:27.255635347508175%; --time:3.921324469905532s; --delay:-2.522232052071663s;"></div>
                    <div class="bubble" style="--size:3.529319209669098rem; --distance:8.18483145707036rem; --position:69.08950808381277%; --time:2.810504972963296s; --delay:-2.687884706885382s;"></div>
                    <div class="bubble" style="--size:4.335695108035998rem; --distance:9.447361502457419rem; --position:76.22963609741936%; --time:3.03035208795363s; --delay:-3.539730545119888s;"></div>
                    <div class="bubble" style="--size:5.140529420294012rem; --distance:6.46200469225704rem; --position:37.176509947126675%; --time:2.1155034168566034s; --delay:-3.644350944629174s;"></div>
                    <div class="bubble" style="--size:3.5763066863918453rem; --distance:7.497511821444349rem; --position:103.96544520273301%; --time:2.1682090086654306s; --delay:-3.706517743409315s;"></div>
                    <div class="bubble" style="--size:2.1765712586085684rem; --distance:7.075467865854145rem; --position:98.24306636387647%; --time:3.6766525228120894s; --delay:-3.04537597585354s;"></div>
                </div>

                </div>
                <svg style="position:fixed; top:100vh">
                <defs>
                    <filter id="blob">
                    <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="blur"></feGaussianBlur>
                    <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 19 -9" result="blob"></feColorMatrix>
                    <!--feComposite(in="SourceGraphic" in2="blob" operator="atop") //After reviewing this after years I can't remember why I added this but it isn't necessary for the blob effect-->
                    </filter>
                </defs>
                </svg>


        </div>

    </div>

    <div v-if = "!auth">
        <div class = "errorPage">
            error
        </div>
    </div>
</template>

<script>
import { Icon } from '@iconify/vue';
import {onMounted, ref} from 'vue';
import {useStore} from "vuex";
import {useRouter} from "vue-router";
import VsPaginationVue from '../components/VsPagination.vue';
import Multiselect from 'vue-multiselect';


export default {
    name: 'allPublicPost',

    data () {

        return {

            email:'',
            search:'',

            genreList: [
                {name:"comedy", id:1},
                {name:"sci-fi", id:2},
                {name:"horror", id:3},
                {name:"romance", id:4},
                {name:"action", id:5},
                {name:"thriller", id:6},
                {name:"mystery", id:7},
                {name:"crime", id:8},
                {name:"animation", id:9},
                {name:"fantasy", id:10},
            ],
            //for checkboxes
            checkedTypes:[],
            checkedTypes1:[],

        }
    },

    components: {
      Icon,
      VsPaginationVue,
      Multiselect
    },

    methods: {

        async logout(){

            await fetch('http://localhost:8000/logout', {
                method: 'POST',
                mode: 'cors',
                headers: { 'Content-Type': 'application/json' },
                credentials: 'include',

            })
            this.router.push('/login')
        },

        editRoot(rootGet){
            let netRoot = rootGet.replace('/capstone_project_vue/src/assets/', '')
            console.log(netRoot)
            // data.urlString = netRoot
            // document.getElementById('thumb').src()
            return netRoot
        }


    },
    computed:{

        auth(){
            const store = useStore();
            return store.state.authenticated
        },

        filteredPosts(){

            if (!this.checkedTypes1.length) {
                //$('#inputText').prop('disabled', false);
		  		return this.allPosts.filter(item => {
					return item.title.indexOf(this.search) > -1 || item.artist.indexOf(this.search) > -1
		  		});

            } else {
                return this.allPosts.filter(item => {
		  		     return this.checkedTypes1.includes(item.genres[0]);
			    })

            }


        }


    },

    created() {
    },

    setup(){
        const message = ref('You are not logged in!');
        const email = ref('You are not logged in!');
        const allPosts = ref([])
        const router = useRouter()


        onMounted(async () => {

            const store = useStore()

            try {
                const response = await fetch('http://localhost:8000/user', {
                    headers: {'Content-Type': 'application/json'},
                    credentials: 'include'
                });

                //user response after cookie
                const content = await response.json();


                //not optimal code need change later
                if (content == 'Unauthenticated!'){

                    await store.dispatch('setAuth', false);

                } else {
                    message.value = `Hi ${content.name}`;
                    email.value = `Hi ${content.email}`;

                    await store.dispatch('setAuth', true);

                    //getting the account id of an individual user
                    console.log(content.id)
                    await fetch("http://localhost:8000/Account/" + content.id +"/get_account/", {
                            headers: {'Content-Type': 'application/json'},
                            credentials: 'include'
                    })
                    .then((response) => response.json())
                    .then((account) => {
                        console.log(account)
                        store.dispatch('setAccountID', account[0].account_id);
                    })



                    //fetching all posts belonging to individual user
                    await fetch("http://localhost:8000/Record/get_all_records/", {
                            headers: {'Content-Type': 'application/json'},
                            credentials: 'include'
                    })

                    .then((response) => response.json())
                    .then( function(result){

                        console.log('Result', result)

                        for (var i = 0; i < result.length; i++) {
                            console.log(result[i])
                            allPosts.value.push(result[i])
                        }

                        console.log(allPosts)

                    })


                    //was for vuex testing
                    //await store.dispatch('setUserID', content.id);

                }

            } catch (e) {

                await store.dispatch('setAuth', false);
            }


        });


        return {
            message,
            email,
            allPosts,
            router

        }


    }



}
</script>



<style>

@import '../assets/styles/homePage.css';

</style>